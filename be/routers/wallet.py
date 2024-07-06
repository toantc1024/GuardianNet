from fastapi import APIRouter, HTTPException, Form
from bson import ObjectId
from models.wallet import Wallet, Transaction
from constant import Constants
from datetime import datetime

router = APIRouter(prefix="/api/guardiannet", tags=["Wallet"])

@router.post("/create_wallet")
async def create_wallet(email: str = Form(..., description="Email address of the user")):
    user = Constants.USERS.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user_id = str(user["_id"])
    existing_wallet = Constants.WALLETS.find_one({"user_id": ObjectId(user_id)})
    if existing_wallet:
        raise HTTPException(status_code=409, detail="Wallet already exists")

    wallet = Wallet(
        user_id=ObjectId(user_id),
        balance=0.0,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    Constants.WALLETS.insert_one(wallet.dict())

    return {"message": "Wallet created successfully", "wallet": wallet.dict()}

@router.post("/add_money")
async def add_money(
    email: str = Form(..., description="Email address of the user"),
    amount: float = Form(..., description="Amount to add")
):
    user = Constants.USERS.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user_id = str(user["_id"])
    wallet = Constants.WALLETS.find_one({"user_id": ObjectId(user_id)})
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")

    new_balance = wallet["balance"] + amount

    Constants.WALLETS.update_one(
        {"user_id": ObjectId(user_id)},
        {"$set": {"balance": new_balance, "updated_at": datetime.utcnow()}}
    )

    transaction = Transaction(
        user_id=ObjectId(user_id),
        amount=amount,
        type="credit",
        created_at=datetime.utcnow()
    )

    Constants.TRANSACTIONS.insert_one(transaction.dict())

    return {"message": "Money added successfully", "new_balance": new_balance}

@router.post("/spend_money")
async def spend_money(
    email: str = Form(..., description="Email address of the user"),
    amount: float = Form(..., description="Amount to spend")
):
    user = Constants.USERS.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user_id = str(user["_id"])
    wallet = Constants.WALLETS.find_one({"user_id": ObjectId(user_id)})
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")

    if wallet["balance"] < amount:
        raise HTTPException(status_code=400, detail="Insufficient balance")

    new_balance = wallet["balance"] - amount

    Constants.WALLETS.update_one(
        {"user_id": ObjectId(user_id)},
        {"$set": {"balance": new_balance, "updated_at": datetime.utcnow()}}
    )

    transaction = Transaction(
        user_id=ObjectId(user_id),
        amount=amount,
        type="debit",
        created_at=datetime.utcnow()
    )

    Constants.TRANSACTIONS.insert_one(transaction.dict())

    return {"message": "Money spent successfully", "new_balance": new_balance}
