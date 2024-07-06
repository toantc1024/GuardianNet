from fastapi import FastAPI, HTTPException
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import base64

app = FastAPI()

# Load credentials from service account key file (JSON)
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
SERVICE_ACCOUNT_FILE = 'path_to_your_service_account_key.json'

# Initialize Gmail API service
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
gmail_service = build('gmail', 'v1', credentials=credentials)

# Endpoint to retrieve content accessed by Gmail account within a day
@app.get("/monitor/gmail_content/{user_email}", response_model=list)
async def monitor_gmail_content(user_email: str):
    try:
        # Calculate date range (from yesterday to today)
        today = datetime.utcnow()
        yesterday = today - timedelta(days=1)
        yesterday_str = yesterday.strftime('%Y/%m/%d')

        # List messages in the user's account within the date range
        query = f"after:{yesterday_str}"
        messages = gmail_service.users().messages().list(userId=user_email, q=query).execute()
        
        # Extract message IDs
        message_ids = [message['id'] for message in messages.get('messages', [])]
        
        # Retrieve content from each message
        accessed_content = []
        for message_id in message_ids:
            message = gmail_service.users().messages().get(userId=user_email, id=message_id).execute()
            payload = message['payload']
            if 'parts' in payload:
                for part in payload['parts']:
                    if 'body' in part:
                        body = part['body']
                        if 'data' in body:
                            content = body['data']
                            # Decode content from base64
                            decoded_content = base64.urlsafe_b64decode(content).decode('utf-8')
                            accessed_content.append(decoded_content)
        
        return accessed_content
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving content: {str(e)}")
