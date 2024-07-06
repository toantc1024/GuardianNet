# -*- coding: utf-8 -*-
import logging


import logging_setup  # setup logging
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import register, login, activate_account

logger = logging.getLogger("Backend")


app = FastAPI( docs_url="/api/guardiannet/docs")

origins = [
    "http://localhost",
    # "http://localhost:{fe port}",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.get("/")(lambda: {"message": "Welcome to GuardianNet!!!!!!!!!!"})

app.include_router(register.router)
app.include_router(login.router)
app.include_router(activate_account.router)

if __name__ == "__main__":
    uvicorn.run("main:app", workers=-1, host="0.0.0.0", port=8080)