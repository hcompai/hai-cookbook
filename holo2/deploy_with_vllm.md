# How to Deploy Holo2 (4B, 8B, or 30B-A3B) Locally with vLLM on NVIDIA GPUs

## Run a vLLM Server Locally

### Requirements
- An **NVIDIA GPU** with drivers installed  

### Installation
1. Install vLLM using the instructions provided by [vLLM](https://docs.vllm.ai/en/latest/getting_started/installation/index.html)


### Example

You can launch vllm from the command line after installation. vllm 0.11.1 or higher is required for having acces to latest reasoning parsers. 

```
vllm serve Hcompany/Holo2-4B \
    --dtype bfloat16 \
    --gpu-memory-utilization 0.9 \
    --max-model-len=65536 \
    --reasoning-parser=deepseek_r1
    --limit-mm-per-prompt={"image": 3, "video": 0} \
    --max-model-len 16384
```

## Deploy via Docker

### Requirements

- An **NVIDIA GPU** with drivers installed  
- [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit) to allow Docker to access your GPU  
- [Docker](https://docs.docker.com/get-docker/) installed and running  


### Example: Run Holo2 4B

```
docker run -it --gpus=all --rm -p 8000:8000 vllm/vllm-openai:v0.11.1 \
    --model Hcompany/Holo2-4B \
    --dtype bfloat16 \
    --gpu-memory-utilization 0.9 \
    --max-model-len=65536 \
    --reasoning-parser=deepseek_r1
    --limit-mm-per-prompt={"image": 3, "video": 0} \
    --max-model-len 16384
```

- 💡 To run Holo2 8B, change --model to HCompany/Holo2-8B.
- 💡 To run Holo2 30B A3B, change --model to HCompany/Holo2-30B-3AB and add --tensor-parallel-size 2

## Invoking Holo2 via API

When vLLM is running, you can send requests to:

```
http://localhost:8000/v1/chat/completions
```

### Test with curl

```
curl http://localhost:8000/v1/chat/completions     -H "Content-Type: application/json"     -d '{
        "model": "HCompany/Holo2-4B",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"}
        ]
        "extra_body": {
            "chat_template_kwargs": {
                "thinking": True 
            }
        }
    }'
```

### Test with Python (OpenAI SDK)

1. Install OpenAI client:

```
pip install openai
```

2. Example Python script:

```Python
from openai import OpenAI

BASE_URL = "http://localhost:8000/v1"
API_KEY = "EMPTY"
MODEL = "HCompany/Holo2-4B"
ENABLE_THINKING = True

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)

chat_completion = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"}
    ]
    # Toggle reasoning if vllm is configured with deepseek_v3 reasoning parser.
    # This extra body has not effect if deepseek_r1 reasoning parser is used. 
    extra_body={"chat_template_kwargs": {"thinking": ENABLE_THINKING }}
)

print(chat_completion.choices[0].message.content)
```

🔐 Note: The API key is not used by vLLM, but required by the OpenAI SDK — use "EMPTY" as a placeholder.

### Notes
- `--model` can be set to `HCompany/Holo2-4B`, `HCompany/Holo2-8B` or `HCompany/Holo2-30B-A3B`
- `--gpus=all` enables all NVIDIA GPUs for the container.
- `--tensor-parallel-size` must be greater than 2 for `HCompany/Holo2-30B-A3B`
- Holo2 is a multimodal model, so you can adjust image limits using `--limit-mm-per-prompt`.
- Reduce `--max-model-len` or `--gpu-memory-utilization` if your GPU runs out of memory.
- Ensure your GPU supports bfloat16 (e.g., H100, A100, L40S, RTX 4090, etc.), use float16 otherwise.
- Port 8000 must be free; change it with `-p <host>:8000` if needed.

## Holo2 reasoning parser compatibility

Holo2 models are reasoning models. In order to extract reasoning content for a request, we need to set the reasoning_parser accordingly in vllm (docker or vllm serve). 

Holo2 chat template is configurable to enable and disable thinking. It can be done at the request level by providing chat template kwargs in the openai request payload. 

Here the compatibility grid for `--reasoning-parser` arg

Parser      | Features
deepseek_r1 | Thinking mode only; structured output supported
deepseek_v3 | Thinking mode toggleable; no structured output. Chat template args must be provided on all requests


## Examples

When, the endpoint is in service, you can re-use our hosted api examples by replacing the base_url and model field with the proper values. 

- [Holo2 Localization with HAI API](https://github.com/hcompai/hai-cookbook/blob/main/holo2/holo_2_localization_hosted_api.ipynb)