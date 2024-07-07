from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# Example model for web access data
class WebAccessData(BaseModel):
    user_id: str
    web_url: str
    title: str
    access_time: str

