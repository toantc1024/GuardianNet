# -*- coding: utf-8 -*-
from fastapi import APIRouter, Form, HTTPException
from fastapi.responses import JSONResponse
from constant import Message, Constants
from pymongo import MongoClient
import bcrypt
from datetime import datetime, timedelta
from utils.token import unique_string

from pydantic import BaseModel
router = APIRouter(prefix="/api/guardiannet", tags=["User Login"])

class Login(BaseModel):
    username: str
    password: str

@router.post("/login", responses={401: {"model": Message}, 404: {"model": Message}})
def login(
 data: Login
):
    # Find the user account in the database
    account = Constants.USERS.find_one({"username": data.username})
    
    if account:
        # Compare the entered password with the stored hashed password
        if bcrypt.checkpw(data.password.encode("utf-8"), account["password"].encode("utf-8")):
            # Return user details if the password matches
            return JSONResponse(
                content={
                    "user_id": str(account["_id"]),
                    "username": account["username"],
                    "age": account.get("age"),
                    "role": account.get("role"),
                    "is_subscribed": account.get("is_subscribed"),
                    "wallet_address": account.get("wallet_address")
                }
            )
        else:
            return JSONResponse(
                status_code=401, content={"message": "Password is incorrect."}
            )
    else:
        return JSONResponse(
            status_code=404, content={"message": "User does not exist."}
        )

