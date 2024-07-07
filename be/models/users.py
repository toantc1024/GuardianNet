# -*- coding: utf-8 -*-
from __future__ import annotations

from pydantic import BaseModel, Field, EmailStr, validator
from datetime import datetime
from email_validator import validate_email
from typing_extensions import Annotated
from pymongo import ReturnDocument
from bson import ObjectId
from typing import Optional


class UserInfo(BaseModel):
    """
    Object to describe User Information
    """

    username: str = Field(..., description="Username of the user")
    password: str = Field(..., description="Password of the user")
    age: int = Field(..., description="Age")
    role: str = Field(..., description="Bussiness or normal account")
    is_subcribed: Optional[bool] = Field(False, description="Subcribed or not")   
    wallet_address: Optional[str] =  Field('', description="Wallet address")

    def get_context_string(self, context: str):
        return f"{context}{self.password[-6:]}{self.updated_at.strftime('%m%d%Y%H%M%S')}".strip()

    @validator("username")
    def validate_username(cls, v):
        if any(char.isspace() or not char.isalnum() for char in v):
            raise ValueError(
                "Username should not contain spaces or special characters."
            )
        return v
