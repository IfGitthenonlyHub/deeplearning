# src/scripts/fine_tune_uet_coder.py

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer, DataCollatorForLanguageModeling
from datasets import load_dataset
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
import os

# 1. Cấu hình mô hình và đường dẫn
model_name = "Qwen/Qwen2.5-Coder-3B-Instruct" 
output_dir = "./models/uet_coder_finetuned_model" 
train_data_path = "./data/processed/train_data.jsonl" 

# 2. Tải Tokenizer và Mô hình Base
print(f"Loading tokenizer from {model_name}...")
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token
print("Tokenizer loaded.")

# Đặt padding_side của tokenizer là "right" cho training
tokenizer.padding_side = "right"

print(f"Loading model from {model_name} with 4-bit quantization...")
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16, # Sử dụng float16 cho RTX 3050M
    device_map="auto",
    load_in_4bit=True, 
    trust_remote_code=True, # Cần cho Qwen2.5-Coder
)
model = prepare_model_for_kbit_training(model)
print("Model loaded and prepared for k-bit training.")

# 3. Cấu hình LoRA
lora_config = LoraConfig(
    r=16, 
    lora_alpha=32,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"], 
    bias="none",
    lora_dropout=0.05,
    task_type="CAUSAL_LM",
)
model = get_peft_model(model, lora_config)
print("LoRA configured and applied to the model.")
model.print_trainable_parameters() 

# 4. Tải và xử lý dữ liệu huấn luyện
print(f"Loading dataset from {train_data_path}...")
dataset = load_dataset("json", data_files=train_data_path, split="train")

def tokenize_function(examples):
    # max_length cần đủ lớn để chứa cả problem và solution.
    # Nếu bài toán + lời giải quá dài, nó sẽ bị cắt bớt (truncation=True).
    return tokenizer(examples["text"], truncation=True, max_length=1024) 

tokenized_dataset = dataset.map(tokenize_function, batched=True, remove_columns=["text"])
print("Dataset tokenized.")

data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# 5. Cấu hình Huấn luyện
training_args = TrainingArguments(
    output_dir=output_dir,
    num_train_epochs=2, # Tăng số epoch nếu cần
    per_device_train_batch_size=1, 
    gradient_accumulation_steps=4, 
    learning_rate=1e-4, 
    logging_steps=10, 
    save_steps=200, 
    report_to="none",
    fp16=True, 
    optim="paged_adamw_8bit", 
    remove_unused_columns=False,
    gradient_checkpointing=True, 
    gradient_checkpointing_kwargs={'use_reentrant':False},
    overwrite_output_dir=True, # Ghi đè thư mục output nếu đã tồn tại
)

# 6. Khởi tạo và Bắt đầu Huấn luyện
print("Initializing Trainer...")
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    tokenizer=tokenizer,
    data_collator=data_collator,
)

print("Starting training...")
trainer.train()
print("Training finished.")

# 7. Lưu mô hình đã fine-tune
final_model = trainer.model
final_model.save_pretrained(output_dir)
tokenizer.save_pretrained(output_dir)
print(f"Fine-tuned model and tokenizer saved to {output_dir}")