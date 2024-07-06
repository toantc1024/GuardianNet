from fastapi import APIRouter, HTTPException, Form
from fastapi.responses import JSONResponse
from bson import ObjectId
from datetime import datetime, timedelta
from constant import Constants
from models.users import UserInfo

router = APIRouter(prefix="/api/guardiannet", tags=["Subscription"])

@router.post("/subscribe")
async def subscribe(user_id: str = Form(..., description="User ID of the user")):
    try:
        # Find the user in the database
        user = Constants.USERS.find_one({"_id": ObjectId(user_id)})
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        # Calculate subscription start and end times
        subscription_start = datetime.utcnow()
        subscription_end = subscription_start + timedelta(days=30)

        # Update the user's subscription status and times
        Constants.USERS.update_one(
            {"_id": ObjectId(user_id)},
            {
                "$set": {
                    "is_subscribed": True,
                    "subscription_start": subscription_start,
                    "subscription_end": subscription_end,
                }
            }
        )

        return JSONResponse(content={"message": "Subscription activated", "subscription_start": subscription_start, "subscription_end": subscription_end})

    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})

