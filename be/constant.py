# -*- coding: utf-8 -*-
import certifi
import os
import urllib.parse

from pydantic import BaseModel

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv(os.path.join(os.path.dirname(__file__), ".env.example"))


class Constants:
    MONGODB_URI = "mongodb+srv://mylittlehusky2004:9IQxDk7sxq61sgof@cluster1.leyhjsm.mongodb.net/?appName=Cluster1"

    parsed_uri = urllib.parse.urlparse(MONGODB_URI)
    encoded_uri = MONGODB_URI.replace(
        parsed_uri.username, urllib.parse.quote_plus(parsed_uri.username)
    )
    encoded_uri = encoded_uri.replace(
        parsed_uri.password, urllib.parse.quote_plus(parsed_uri.password)
    )
    # Create MongoDB client
    client = MongoClient(host=encoded_uri, tlsCAFile=certifi.where(), tls=True)

    # Get the database
    db = client.get_database("Cluster1")

    # Get collections
    USERS = db.get_collection("USERS")
    USER_TOKENS = db.get_collection("USER_TOKENS")
    WEB_ACCESS = db.get_collection("WEB_ACCESS")
# Define Message class
class Message(BaseModel):
    message: str