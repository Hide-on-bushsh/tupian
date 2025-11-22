import requests

url = "http://127.0.0.1:30000"

payload = {
    "model": "/data1/models/bge-m3",
    "input": "What is the capital of France?",
    "encoding_format": "float"
}

response = requests.post(url + "/v1/embeddings", json=payload).json()
embedding = response["data"][0]["embedding"]

payload = {
    "model": "/data1/models/bge-m3",
    "input": "What is the capital of BeiJing?",
    "encoding_format": "float"
}

response1 = requests.post(url + "/v1/embeddings", json=payload).json()
embedding1 = response1["data"][0]["embedding"]
for a,b in zip(embedding, embedding1):
    print(f"{a-b}\t{a}\t{b}")
