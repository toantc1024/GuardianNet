from pydantic import BaseModel
from bson import ObjectId
from typing import Optional
from datetime import datetime

class Wallet(BaseModel):
    user_id: str
    created_at: datetime

class Widthdraw(BaseModel):
    wallet_address: str
    widthdraw_time: datetime
