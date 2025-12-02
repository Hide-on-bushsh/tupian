curl http://127.0.0.1:8080/generate \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "text": "<|user|>\n什么是奖励模型？\n<|assistant|>\n奖励模型用于评估对话质量，为对齐提供反馈。",
    "sampling_params": {
      "max_new_tokens": 1,
      "temperature": 0
    },
    "return_logits": true
  }'