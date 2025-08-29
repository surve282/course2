#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "24548240"))
API_HASH = environ.get("API_HASH", "f64dbe9639fa7b92368b045a33110d9c")
BOT_TOKEN = environ.get("BOT_TOKEN", "8381100179:AAH6CWfPmwBJ5bAqGZnkhfysF-v2ZaTkyYo")
OWNER = int(environ.get("OWNER", "1363113279"))
CREDIT = "SS2"
AUTH_USER = os.environ.get('AUTH_USERS', '').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set


