from pydantic import BaseModel
from bson import ObjectId
from typing import Optional
from datetime import datetime

class Wallet(BaseModel):
    user_id: str
    balance: float
    created_at: datetime
    updated_at: datetime

class Transaction(BaseModel):
    user_id: str
    amount: float
    type: str  # 'credit' or 'debit'
    created_at: datetime
