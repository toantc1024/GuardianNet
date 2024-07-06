# -*- coding: utf-8 -*-
import jwt
import os
import uuid

from fastapi import APIRouter, Form, BackgroundTasks, HTTPException
from fastapi.responses import JSONResponse
from models.users import UserInfo
from constant import Message, Constants
import bcrypt
from datetime import datetime, timedelta


router = APIRouter(prefix="/api/guardiannet", tags=["User Register"])


@router.post("/register", responses={409: {"model": Message}, 422: {"model": Message}})
def register_user(
    background_tasks: BackgroundTasks,
    user_name: str = Form(..., description="Username of the user"),
    password: str = Form(..., description="Password of the user"),
    age: int = Form(..., description="Age of the user"),
    role: str = Form(..., description="Role of the user"),
):
    try:
        # Check if username is already used
        if Constants.USERS.find_one({"username": user_name}):
            raise HTTPException(status_code=409, detail="Username already used.")

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        # Create UserInfo object
        user_info = UserInfo(
            username=user_name,
            password=hashed_password,
            age=age,
            is_subscribed=False,  
            role=role,
            wallet_address="null",
        )
        user_info_dict = user_info.dict()

        # Insert user info into database
        Constants.USERS.insert_one(user_info_dict)

    except HTTPException as e:
        raise e
    except Exception as e:
        # Handle other unexpected errors
        return JSONResponse(status_code=422, content={"message": str(e)})

    # Return success response without returning the password
    return JSONResponse(
        content={
            "user_name": user_name,
            "age": age,
            "is_subscribed": user_info.is_subscribed,
            "role": role,
        }
    )




