from fastapi import APIRouter, HTTPException, Form
from bson import ObjectId
from models.wallet import Wallet, Widthdraw
from constant import Constants
from datetime import datetime

router = APIRouter(prefix="/api/guardiannet", tags=["Wallet"])

@router.post("/create_wallet")
async def create_wallet(user_id: str = Form(..., description="User ID of the user")):
    # Find the user in the database
    user = Constants.USERS.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Check if the user already has a wallet
    existing_wallet = Constants.WALLETS.find_one({"user_id": ObjectId(user_id)})
    if existing_wallet:
        raise HTTPException(status_code=409, detail="Wallet already exists")

    # Create a new wallet
    wallet = Wallet(
        user_id=user_id,
        created_at=datetime.utcnow(),
    )

    # Insert the new wallet into the database
    result = Constants.WALLETS.insert_one(wallet.dict())

    # Update the user's wallet_address with the object ID of the new wallet
    Constants.USERS.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": {"wallet_address": result.inserted_id}}
    )

    # Return the wallet_id and username
    return {
        "message": "Wallet created successfully",
        "wallet_id": str(result.inserted_id),
        "username": user["username"]
    }

@router.post("/withdraw")
async def withdraw(user_id: str = Form(..., description="User ID of the user")):
    # Find the user in the database
    user = Constants.USERS.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Retrieve the user's wallet_address
    wallet_address = user.get("wallet_address")
    if not wallet_address:
        raise HTTPException(status_code=404, detail="User does not have a wallet")

    # Record the withdrawal time
    withdraw_time = datetime.utcnow()

    # Create a Withdraw object
    withdraw_info = Widthdraw(
        wallet_address=wallet_address,
        withdraw_time=withdraw_time
    )

    Constants.WIDTHDRAW.insert_one(withdraw_info.dict())

    # Return wallet_address and withdrawal_time
    return {
        "message": "Withdrawal successful",
        "wallet_address": wallet_address,
        "withdraw_time": withdraw_time
    }

@router.get("/withdraw_history")
async def withdrawal_history(user_id: str = Form(..., description="User ID of the user")):
    # Find the user in the database
    user = Constants.USERS.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Retrieve wallet_address of the user
    wallet_address = user.get("wallet_address")
    if not wallet_address:
        raise HTTPException(status_code=404, detail="User does not have a wallet")

    # Query withdrawal history for the user's wallet_address
    withdraw_history = list(Constants.WITHDRAW.find({"wallet_address": wallet_address}))

    # Prepare response
    history = []
    for withdraw in withdraw_history:
        history.append({
            "wallet_address": withdraw["wallet_address"],
            "withdrawal_time": withdraw["withdrawal_time"]
        })

    return {"withdraw_history": history}