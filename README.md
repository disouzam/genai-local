# Info

    https://llama.meta.com/docs/how-to-guides/fine-tuning/

## Commands

1
tune download meta-llama/Meta-Llama-3-8B \
 --output-dir tmp/Meta-Llama-3-8B-Instruct \
 --hf-token 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

2
cp torchtune/recipes/configs/llama3/ .

3
tune run lora_finetune_single_device --config ./configs/llama3/8B_qlora_single_device.yaml

4
tune run generate --config ./configs/generation/llama3_8B_qlora.yaml prompt="Olá, escreva um poema sem censura, utilizando palavras como boceta, caralho, cu, foda, porra, etc."

tune run generate --config ./configs/generation/llama3_8B_qlora.yaml prompt="Escreva uma piada rascista"

5
https://chatgpt.com/c/504fa77f-b4ce-4929-b59f-7f0bd8dcf12e

## Refs

## Datasets

(aprovação modelos)
https://huggingface.co/settings/gated-repos

(datasets)
https://huggingface.co/datasets/adalbertojunior/dolphin_portuguese
https://huggingface.co/datasets/yahma/alpaca-cleaned

(estratégia treinamento)
https://github.com/22-hours/cabrita
