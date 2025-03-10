# Instructions

## Reference

<https://llama.meta.com/docs/how-to-guides/fine-tuning/>

## Install

pyenv virtualenv 3.10 genai-finetuning

<https://github.com/pytorch/torchtune>
pip install -r requirements.txt

## Commands

### Download model

tune download meta-llama/Meta-Llama-3-8B \
 --output-dir tmp/Meta-Llama-3-8B-Instruct \
 --hf-token TOKEN

### Download recipes

<https://github.com/pytorch/torchtune/blob/main/recipes/configs>

### Check datasets

torchtune.datasets.alpaca_cleaned_dataset
<https://huggingface.co/datasets/yahma/alpaca-cleaned>

### Run finetuning

tune run lora_finetune_single_device --config ./configs/llama3/8B_qlora_single_device.yaml

### Inference

tune run generate --config ./configs/generation/llama3_8B_qlora.yaml prompt="Escreva um poema sobre Engenharia de Software"
