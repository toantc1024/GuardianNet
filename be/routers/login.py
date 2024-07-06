# -*- coding: utf-8 -*-
from fastapi import APIRouter, Form, HTTPException
from fastapi.responses import JSONResponse
from constant import Message, Constants
from pymongo import MongoClient
import bcrypt
from datetime import datetime, timedelta
from utils.token import unique_string

router = APIRouter(prefix="/api/guardiannet", tags=["User Login"])


@router.post("/login", responses={401: {"model": Message}, 404: {"model": Message}})
def login(
    username: str = Form(..., description="Username of the user"),
    password: str = Form(..., description="Password of the user"),
):
    # Find the user account in the database
    account = Constants.USERS.find_one({"username": username})
    
    if account:
        # Compare the entered password with the stored hashed password
        if bcrypt.checkpw(password.encode("utf-8"), account["password"].encode("utf-8")):
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

