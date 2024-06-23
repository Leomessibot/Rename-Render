# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "26305156")

API_HASH = os.environ.get("API_HASH", "9937930c368c669ca905e9a95aa712f0")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7317164501:AAE-TiyWBlJaiD-QrVRZhhrXuPQrKF3Ya_c") 

FORCE_SUB = os.environ.get("FORCE_SUB", "moviebot_channel") 

             # Don't Remove Credit @cinemaworld_update 
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @Leomessi_10_19 

DB_NAME = os.environ.get("DB_NAME", "puyoo")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://joyyus:joyyus@puyoo.vc0ax0l.mongodb.net/?retryWrites=true&w=majority&appName=puyoo")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/3eb1358499627bb672e84.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '7040444713').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @cinemaworld_update 
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @Leomessi_10_19 
