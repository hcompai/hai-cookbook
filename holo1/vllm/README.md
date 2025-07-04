# How to deploy Holo1 (3B or 7B) locally with vLLM on Nvidia 

## Run a vLLM-Server Locally

### Requirements
- An **NVIDIA GPU** with drivers installed  

### Installation
1. Install vLLM using the instructions provided by [vLLM](https://docs.vllm.ai/en/latest/getting_started/installation/index.html)

2. Install a compatible version of `transformers`:

```
pip install "transformers<4.53.0" ≈
```

### Example

```
vllm serve Hcompany/Holo1-3B --port 8000
```

## Deploy via Docker

### Requirements

- An **NVIDIA GPU** with drivers installed  
- [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit) to allow Docker to access your GPU  
- [Docker](https://docs.docker.com/get-docker/) installed and running  


### Example: Run Holo1 3B

```
docker run -it --gpus=all --rm -p 8000:8000 vllm/vllm-openai:v0.9.1 \
    --model HCompany/Holo1-3B \
    --dtype bfloat16 \
    --gpu-memory-utilization 0.9 \
    --limit-mm-per-prompt 'image=3,video=0' \
    --mm-processor-kwargs '{"max_pixels": 1003520}' \
    --max-model-len 16384
```

💡 To run Holo1 7B, change --model to HCompany/Holo1-7B.

### Invoking Holo1 via API

After the container is running, you can send requests to:

```
http://localhost:8000/v1/chat/completions
```

### Test with curl

```
curl http://localhost:8000/v1/chat/completions     -H "Content-Type: application/json"     -d '{
        "model": "HCompany/Holo1-3B",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"}
        ]
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
MODEL = "HCompany/Holo1-3B"

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
)

print(chat_completion.choices[0].message.content)
```

🔐 Note: The API key is not used by vLLM, but required by the OpenAI SDK — use "EMPTY" as a placeholder.

### Notes
- `--model` can be set to `HCompany/Holo1-3B` or `# HCompany/Holo1-7B`
- `--gpus=all` enables all NVIDIA GPUs for the container.
- Holo1 is a multimodal model, so you can adjust image/video limits using `--limit-mm-per-prompt`.
- Reduce `--max-model-len` or `--gpu-memory-utilization` if your GPU runs out of memory.
- Ensure your GPU supports bfloat16 (e.g., A100, L40S, RTX 4090, etc.), use float16 otherwise.
- Port 8000 must be free; change it with `-p <host>:8000` if needed.

## Examples

The endpoint is in service. You can use OpenAI Client to perform real time inference on the deployed Holo-1 model.

- [Using OpenAI Client to invoke Holo1 for a navigation task](https://github.com/hcompai/hai-cookbook/blob/main/holo1/vllm/invoke_navigation.ipynb)
- [Using OpenAI Client to invoke Holo1 for a localization task](https://github.com/hcompai/hai-cookbook/blob/main/holo1/vllm/invoke_localization.ipynb)