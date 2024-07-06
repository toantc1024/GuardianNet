from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Example model for web activity
class WebActivity(BaseModel):
    user_email: str
    accessed_url: str
    content_type: str  # Optional: categorize content type

# Dummy storage for monitored activities
monitored_activities = []

# Endpoint to receive and store web activities
@app.post("/monitor/web_activity", response_model=WebActivity)
async def monitor_web_activity(activity: WebActivity):
    # Example: Store monitored activity
    monitored_activities.append(activity)
    return activity
