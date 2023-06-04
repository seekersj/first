import requests
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def show():
    return {"Sujin": "Hello:)"}

@app.post("/chat")
async def chat(question: str):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "덕성초 4학년 친구들, 기사문 단어들이 어려워 이해가 되지 않나요? 내가 도와줄게요. 아래에 기사문의 글을 붙여넣어보세요. "},
            {"role": "user", "content": question}
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()
    answer = response_json["choices"][0]["message"]["content"]
    return  {"answer": answer}
