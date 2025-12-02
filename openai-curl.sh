curl http://127.0.0.1:8080/v1/completions \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Skywork/Skywork-Reward-Gemma-2-27B-v0.2",
    "prompt": "<|user|>\n你好\n<|assistant|>\n我很好。",
    "max_tokens": 1,
    "temperature": 0,
    "logprobs": 1  // 返回token的对数概率（非直接奖励分）
  }'