import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / '.env')

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-change-me' #sets the secret key to SECRET_KEY

    WTF_CSRF_ENABLED = True