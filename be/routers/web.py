from fastapi import APIRouter, HTTPException, Form
from fastapi.responses import JSONResponse
from bson import ObjectId
from typing import List
from datetime import datetime
from models.web import WebAccessData
from constant import Message, Constants


router = APIRouter(prefix="/api/guardiannet", tags=["Web Access"])

@router.post("/web_access", responses={409: {"model": Message}, 422: {"model": Message}})
async def web_access(
    user_id: str = Form(..., description="Username of the user"),
    web_url: str = Form(..., description="URL of the website"),
    title: str = Form(..., description="Title of the website"),
    access_time: str = Form(..., description="Time of access")
):
    try:

        web_access_info = WebAccessData(
            user_id=user_id,
            web_url=web_url,
            title=title,
            access_time=datetime.strptime(access_time, '%Y-%m-%d %H:%M:%S'),
        )
        web_access_info_dict = web_access_info.dict()
        Constants.WEB_ACCESS.insert_one(web_access_info_dict)

        return JSONResponse(
            content={
                "user_id": user_id,
                "web_url": web_url,
                "title": title,
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
    
@router.get("/web_access/{user_id}", response_model=List[WebAccessData])
async def get_web_access_records(user_id: str):
    try:
        # Find web access records for the specified user_id
        web_access_records = list(Constants.WEB_ACCESS.find({"user_id": user_id}))
        
        if not web_access_records:
            raise HTTPException(
                status_code=404,
                detail="No web access records found for this user",
            )

        return JSONResponse(content=web_access_records)
    
    except Exception as e:
        return JSONResponse(
            status_code=500, content={"message": str(e)}
        )
    
@router.get("/web_access/all", response_model=List[WebAccessData])
async def get_all_web_access_records():
    try:
        # Retrieve all web access records
        all_web_access_records = list(Constants.WEB_ACCESS.find({}))
        
        if not all_web_access_records:
            raise HTTPException(
                status_code=404,
                detail="No web access records found in the database",
            )

        return JSONResponse(content=all_web_access_records)
    
    except Exception as e:
        return JSONResponse(
            status_code=500, content={"message": str(e)}
        )