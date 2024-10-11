import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer

model_path = "microsoft/Phi-3.5-mini-instruct"

model = AutoModelForCausalLM.from_pretrained(model_path, trust_remote_code=True, torch_dtype=torch.bfloat16).to("cuda")
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True, torch_dtype=torch.bfloat16)

streamer = TextStreamer(tokenizer)

prompt = """
system: {system}
user: {insaan}
assistant:
"""

system = "Você é um chatbot para a disciplina de IA Generativa."
insaan = "Quais linguagens eu posso usar para programar com você?"

prompt = prompt.format(system=system, insaan=insaan)

inputs = tokenizer(prompt, return_tensors="pt", return_attention_mask=True).to("cuda")

model.generate(**inputs, max_length=3084, top_p=0.95, do_sample=True, temperature=0.7, use_cache=True, streamer=streamer)

