from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.database import insert_business_data, get_businesses_by_name
from app.playwright import scrape_business
from typing import List

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/search")
async def search_businesses(business_name: str):
    if not business_name:
        raise HTTPException(status_code=400, detail="Missing business name")
    data = await scrape_business(business_name)
    for d in data:
        insert_business_data(d)
    return get_businesses_by_name(business_name)

@app.get("/api/businesses")
async def get_businesses(q: str = ""):
    return get_businesses_by_name(q)
