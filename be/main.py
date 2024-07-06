# -*- coding: utf-8 -*-
import logging


import logging_setup  # setup logging
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import register, login, web, wallet, subcription
from routers.check_sub import check_subscription_status

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
app.include_router(web.router)
app.include_router(wallet.router)
app.include_router(subcription.router)

check_subscription_status()

if __name__ == "__main__":
    uvicorn.run("main:app", workers=-1, host="0.0.0.0", port=8080)
