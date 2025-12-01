import requests

url = "http://127.0.0.1:8080"

payload = {
    "model": "/data1/models/bge-m3",
    "input": "How are you",
    "encoding_format": "float"
}

response = requests.post(url + "/v1/embeddings", json=payload).json()
embedding = response["data"][0]["embedding"]

payload1 = {
    "model": "/data1/models/bge-m3",
    "input": "I am fine",
    "encoding_format": "float"
}

response1 = requests.post(url + "/v1/embeddings", json=payload1).json()
embedding1 = response1["data"][0]["embedding"]
for a,b in zip(embedding, embedding1):
    print(f"{a-b}\t{a}\t{b}")
