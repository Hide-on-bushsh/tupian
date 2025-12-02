import requests

url = "http://127.0.0.1:8080/generate"
payload = {
    "text": "<|user|>\n介绍一下大模型对齐\n<|assistant|>\n大模型对齐通过奖励模型和RLHF，让模型输出符合人类偏好。",
    "sampling_params": {
        "max_new_tokens": 1,
        "temperature": 0
    },
    "return_logits": True
}

response = requests.post(url, json=payload)
result = response.json()

# 正确提取奖励分数
reward_score = result["logits"][0][0]
print(f"奖励分数：{reward_score}")