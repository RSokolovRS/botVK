import os
from dotenv import load_dotenv, find_dotenv
import requests

load_dotenv(find_dotenv())

API_KEY = os.environ.get("TOKEN")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")

print(DATABASE_PASSWORD)
# print(os.listdir(path="bot_vk"))