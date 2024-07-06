from fastapi import APIRouter, HTTPException, Form
from fastapi.responses import JSONResponse
from bson import ObjectId
from datetime import datetime
from models.web import WebAccessData
from constant import Message, Constants


router = APIRouter(prefix="/api/guardiannet", tags=["Web Access"])

@router.post("/web_access", responses={409: {"model": Message}, 422: {"model": Message}})
async def web_access(
    user_name: str = Form(..., description="Username of the user"),
    email: str = Form(..., description="Email address of the user"),
    web_url: str = Form(..., description="URL of the website"),
    title: str = Form(..., description="Title of the website"),
    access_time: str = Form(..., description="Time of access")
):
    try:
        existing_user = Constants.USERS.find_one({"email": email})
        if existing_user:
            if existing_user.get("role") == "business":
                raise HTTPException(
                    status_code=409,
                    detail="This is not a user account",
                )
        else:
            raise HTTPException(
                status_code=404,
                detail="User not found",
            )

        user_id = str(existing_user["_id"])

        web_access_info = WebAccessData(
            user_id=user_id,
            username=user_name,
            email=email,
            web_url=web_url,
            title=title,
            access_time=datetime.strptime(access_time, '%Y-%m-%d %H:%M:%S'),
        )
        web_access_info_dict = web_access_info.dict()
        Constants.WEB_ACCESS.insert_one(web_access_info_dict)

        return JSONResponse(
            content={
                "user_name": user_name,
                "web_url": web_url,
                "title": title,
                "email": email,
                "user_id": user_id,
                "access_time": access_time
            }
        )
    except ValueError as e:
        # Handle Pydantic validation errors
        return JSONResponse(
            status_code=422, content={"message": str(e)}
        )
    except Exception as e:
        # Handle any other exceptions
        return JSONResponse(
            status_code=500, content={"message": str(e)}
        )