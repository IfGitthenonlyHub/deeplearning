# src/scripts/prepare_training_data.py

import os
import json
import base64
import re # Vẫn cần để giải mã base64

def decode_solution_if_encoded(solution_content: str) -> str:
    """
    Kiểm tra nếu nội dung solution.py chứa mã base64 và giải mã nó.
    """
    # Regex để tìm chuỗi base64 trong đoạn code `base64.b64decode("...")`
    match = re.search(r'base64\.b64decode\("([^"]+)"\)\.decode\("utf-8", "replace"\)', solution_content)
    if match:
        encoded_str = match.group(1)
        try:
            decoded_code = base64.b64decode(encoded_str).decode("utf-8")
            print(f"  -> Decoded base64 solution.")
            return decoded_code
        except Exception as e:
            print(f"  -> Error decoding base64: {e}. Returning original content.")
            return solution_content
    else:
        # Nếu không tìm thấy pattern base64, trả về nội dung gốc
        return solution_content

def prepare_training_data(raw_data_dir: str, processed_data_dir: str, output_filename: str = "train_data.jsonl"):
    """
    Chuẩn bị dữ liệu huấn luyện từ các file problem.md và solution.py.
    """
    problems_dir = os.path.join(raw_data_dir, "problems")
    solutions_dir = os.path.join(raw_data_dir, "solutions")
    output_filepath = os.path.join(processed_data_dir, output_filename)

    if not os.path.exists(processed_data_dir):
        os.makedirs(processed_data_dir)

    training_examples = []
    
    # Lấy danh sách tất cả các file problem.md
    problem_files = sorted([f for f in os.listdir(problems_dir) if f.endswith(".md")])
    
    print(f"Found {len(problem_files)} problem files.")

    for problem_filename in problem_files:
        problem_id = problem_filename.split('.')[0] # Ví dụ: apps_0001
        
        problem_filepath = os.path.join(problems_dir, problem_filename)
        # Các file solution có thể có tiền tố 'apps_' hoặc 'solution_'
        solution_filepath_option1 = os.path.join(solutions_dir, f"{problem_id}.py")
        solution_filepath_option2 = os.path.join(solutions_dir, f"solution_{problem_id.split('_')[-1]}.py")

        solution_filepath = None
        if os.path.exists(solution_filepath_option1):
            solution_filepath = solution_filepath_option1
        elif os.path.exists(solution_filepath_option2):
            solution_filepath = solution_filepath_option2
        else:
            print(f"Warning: No matching solution file found for {problem_id}. Skipping.")
            continue

        print(f"Processing {problem_filename} and {os.path.basename(solution_filepath)}...")

        # Đọc nội dung bài toán
        with open(problem_filepath, "r", encoding="utf-8") as f:
            problem_content = f.read()

        # Đọc nội dung lời giải
        with open(solution_filepath, "r", encoding="utf-8") as f:
            solution_content_raw = f.read()
        
        # Giải mã nếu nội dung là base64
        solution_content_decoded = decode_solution_if_encoded(solution_content_raw)

        # Định dạng mẫu huấn luyện: bọc toàn bộ code đã giải mã vào khối ```python
        final_solution_code_block = f"```python\n{solution_content_decoded.strip()}\n```"

        training_example_text = (
            f"### Problem:\n{problem_content.strip()}\n\n"
            f"### Solution:\n{final_solution_code_block}"
        )
        
        training_examples.append({"text": training_example_text})

    # Ghi các mẫu huấn luyện vào file JSON Lines
    with open(output_filepath, "w", encoding="utf-8") as f:
        for example in training_examples:
            f.write(json.dumps(example) + "\n")
            
    print(f"\nSuccessfully prepared {len(training_examples)} training examples.")
    print(f"Output saved to {output_filepath}")

if __name__ == "__main__":
    RAW_DATA_DIR = "data/raw"
    PROCESSED_DATA_DIR = "data/processed"
    prepare_training_data(RAW_DATA_DIR, PROCESSED_DATA_DIR)