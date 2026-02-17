from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import requests
import redis
import json

load_dotenv()

app = FastAPI(title="AI Wealth Advisor API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

redis_client = redis.from_url(os.getenv("REDIS_URL"))

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"message": "AI Wealth Advisor API", "status": "running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/api/v1/quote/{ticker}")
def get_quote(ticker: str):
    cache_key = f"quote:{ticker}"
    cached = redis_client.get(cache_key)
    if cached:
        return json.loads(cached)
    
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": ticker,
        "apikey": os.getenv("ALPHA_VANTAGE_API_KEY")
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if "Global Quote" in data and data["Global Quote"]:
        quote = data["Global Quote"]
        result = {
            "symbol": quote.get("01. symbol"),
            "price": float(quote.get("05. price", 0)),
            "change": float(quote.get("09. change", 0)),
            "change_percent": quote.get("10. change percent", "0%"),
            "volume": int(quote.get("06. volume", 0))
        }
        redis_client.setex(cache_key, 60, json.dumps(result))
        return result
    raise HTTPException(status_code=404, detail="Quote not found")

@app.post("/api/v1/chat")
def chat_with_advisor(request: ChatRequest):
    message = request.message.lower()
    
    if "retirement" in message:
        response_text = "For retirement, I recommend a diversified portfolio with 60% stocks and 40% bonds."
    elif "portfolio" in message:
        response_text = "A balanced portfolio includes 60% stocks, 30% bonds, and 10% alternatives."
    elif "invest" in message:
        response_text = "Key principles: Start early, diversify, use low-cost index funds, and think long-term."
    else:
        response_text = "I can help with retirement, portfolios, and investing. What would you like to know?"
    
    return {"response": response_text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


