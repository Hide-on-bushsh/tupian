import requests

url = "http://localhost:3000/v1/completions"
payload = {
    "prompt": """<|user|>
什么是奖励模型？
<|assistant|>
奖励模型是一种用于评估生成文本质量的模型，通常为对话模型的对齐阶段提供反馈。
""",
    "max_tokens": 1,
    "return_logits": True,
    "temperature": 0,  # 奖励模型无需采样
}

response = requests.post(url, json=payload)
result = response.json()

# 提取奖励分数
reward_score = result["choices"][0]["logits"][-1][0]
print(f"API调用返回的奖励分数：{reward_score}")