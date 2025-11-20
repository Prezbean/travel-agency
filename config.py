import os, sys
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

if getattr(sys, "frozen", False):
    load_dotenv(Path.cwd() / ".env")

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-change-me' # Sets the secret key to SECRET_KEY

    WTF_CSRF_ENABLED = True