#settings.py
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

API_KEY = print(os.getenv("TOKEN"))
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")

print(API_KEY)
