import requests

def call_openrouter(prompt, api_key, model="meta-llama/llama-2-13b-chat"):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful personal fitness trainer."},
            {"role": "user", "content": prompt}
        ]
    }
    print("Sending request to OpenRouter with:", data)
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]