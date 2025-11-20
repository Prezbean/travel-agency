import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-change-me' # Sets the secret key to SECRET_KEY

    WTF_CSRF_ENABLED = True