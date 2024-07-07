from fastapi import APIRouter, HTTPException, Form
from fastapi.responses import JSONResponse
from bson import ObjectId
from typing import List
from datetime import datetime
from models.web import WebAccessData
from pydantic import BaseModel
from constant import Message, Constants
from db import db



router = APIRouter(prefix="/api/guardiannet", tags=["Web Access"])

class WebAccessItem(BaseModel):
    user_id: str
    web_url: str
    title: str
    access_time: str

@router.get("/web_access", responses={409: {"model": Message}, 422: {"model": Message}})
async def web_access(
    data: WebAccessItem
):
    user_id = data.user_id
    web_url = data.web_url
    title = data.title
    access_time = data.access_time
    
    try:

        web_access_info = WebAccessData(
            user_id=user_id,
            web_url=web_url,
            title=title,
            access_time=access_time
        )
        web_access_info_dict = web_access_info.dict()
        Constants.WEB_ACCESS.insert_one(web_access_info_dict)
        
        db.child("dataset").push({
                "user_id": user_id,
                "web_url": web_url,
                "title": title,
                "access_time": access_time
        })
        
        if(db.child("reward/"+user_id).get().val() == None):
            db.child("reward/"+user_id).set({
                "web_access": 1
            })
        else:
            db.child("reward/"+user_id).update({
                "web_access": db.child("reward/"+user_id).get().val()["web_access"] + 1
            })
        return {
            "message": "Web access record created successfully",
        }

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
    


   
@router.get("/reward/{user_id}", response_model=List[WebAccessData])
async def get_reward_by_userid(user_id):
    try:
        # Retrieve all web access records
        arr = db.child("reward/"+user_id).get()
        
        reward = arr.val()        
        
        return JSONResponse(content={"reward": reward})
    
    except Exception as e:
        return JSONResponse(
            status_code=500, content={"message": str(e)}
        )



   
@router.get("/web_access/all", response_model=List[WebAccessData])
async def get_all_web_access_records():
    try:
        # Retrieve all web access records
        arr = db.child("dataset").get()
        all_web_access_records = []
        for item in arr.each():
            all_web_access_records.append(item.val())
            
        if not all_web_access_records:
            raise HTTPException(
                status_code=404,
                detail="No web access records found in the database",
            )

        return JSONResponse(content={"data": all_web_access_records})
    
    except Exception as e:
        return JSONResponse(
            status_code=500, content={"message": str(e)}
        )

@router.get("/web_access/{user_id}", response_model=List[WebAccessData])
async def get_web_access_records(user_id: str):
    try:
        # Retrieve all web access records
        arr = db.child("dataset").get()
        all_web_access_records = []
        for item in arr.each():
            res = item.val()
            if(res["user_id"] == user_id):
                all_web_access_records.append(res)
                
        if not all_web_access_records:
            raise HTTPException(
                status_code=404,
                detail="No web access records found in the database",
            )
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
 