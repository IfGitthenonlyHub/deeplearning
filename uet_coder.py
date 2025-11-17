# src/uet_coder.py

import argparse
import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import re 

# Đường dẫn tới mô hình đã fine-tune của bạn
FINETUNED_MODEL_PATH = "./models/uet_coder_finetuned_model"
BASE_MODEL_NAME = "Qwen/Qwen2.5-Coder-3B-Instruct" 

# Tải mô hình và tokenizer một lần khi script khởi động
print("Loading tokenizer and base model...")
tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL_NAME)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# Đặt padding_side của tokenizer là "left" cho inference
tokenizer.padding_side = "left"

# Tải mô hình base với lượng tử hóa 4-bit
# Sử dụng torch_dtype=torch.float16 cho RTX 3050M
model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL_NAME,
    torch_dtype=torch.float16, 
    device_map="auto",
    load_in_4bit=True,
    trust_remote_code=True,
)

# Tải các adapter LoRA đã fine-tune và hợp nhất vào mô hình base
model = PeftModel.from_pretrained(model, FINETUNED_MODEL_PATH)
# model = model.merge_and_unload() # Không cần thiết nếu bạn dùng load_in_4bit
print("Fine-tuned model loaded successfully.")


def extract_code_from_generated_text(generated_text: str) -> str:
    """
    Trích xuất code Python từ text được sinh ra, loại bỏ các marker ```python và ```.
    """
    # Tìm kiếm khối code bắt đầu bằng ```python và kết thúc bằng ```
    # Sử dụng DOTALL để . khớp với cả ký tự xuống dòng
    match = re.search(r'```python\s*(.*?)\s*```', generated_text, re.MULTILINE | re.DOTALL)
    if match:
        return match.group(1).strip()
    else:
        # Nếu không tìm thấy khối ```python, có thể mô hình chỉ sinh ra code trực tiếp
        # hoặc có thể nó chỉ sinh ra phần sau input_text.
        # Trong trường hợp này, ta sẽ trả về toàn bộ generated_text sau khi cắt bỏ input_text
        return generated_text.strip()


def generate_solution(problem_description: str) -> str:
    """
    Sử dụng LLM đã fine-tune để sinh ra mã Python.
    """
    # Định dạng input theo cách mô hình đã được huấn luyện
    # Rất quan trọng để khớp với định dạng trong train_data.jsonl
    input_text = f"### Problem:\n{problem_description}\n\n### Solution:\n"

    # Tokenize input
    # max_length cần đủ dài để chứa cả input problem và một phần code boilerplate
    inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True, max_length=1024).to(model.device) 

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=512, # Đặt lại 512, vì lời giải có thể dài hơn
            num_return_sequences=1,
            do_sample=True, # Thử lại sampling để có nhiều lời giải hơn
            temperature=0.7,
            top_p=0.9,
            eos_token_id=tokenizer.eos_token_id,
            pad_token_id=tokenizer.pad_token_id,
            repetition_penalty=1.2,
            # num_beams=5, # Có thể thử Beam Search nếu thời gian cho phép
        )

    full_generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Cắt bỏ phần input_text khỏi kết quả sinh ra để chỉ lấy phần "Solution:"
    # Tìm vị trí bắt đầu của "### Solution:" trong input_text
    solution_start_marker = "### Solution:\n"
    start_of_solution_part_in_input = input_text.find(solution_start_marker) + len(solution_start_marker)
    
    # Cắt phần đầu của full_generated_text tương ứng với input_text
    # Để lại chỉ phần mô hình thực sự sinh ra sau "### Solution:"
    generated_code_with_markers = full_generated_text[len(input_text):].strip()

    # Hậu xử lý để trích xuất chỉ phần code Python (loại bỏ ```python và ```)
    final_solution_code = extract_code_from_generated_text(generated_code_with_markers)
    
    # Đảm bảo hàm generate_solution trả về đúng định nghĩa hàm
    # (nếu code sinh ra là một hàm) hoặc toàn bộ code nếu nó không phải hàm
    # Nhưng theo yêu cầu bài toán, nó phải là một hàm.
    return final_solution_code


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--problem", type=str, required=True,
                        help="Path to the problem description file (Markdown format).")
    parser.add_argument("--output", type=str, required=True,
                        help="Path to the output file where the solution code will be saved.")
    args = parser.parse_args()

    with open(args.problem, "r", encoding="utf-8") as f:
        problem_md = f.read()

    solution_code = generate_solution(problem_md)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(solution_code)

    print(f"Solution generated and saved to {args.output}")