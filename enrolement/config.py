import os

class Config(object):
    SECRET_KY = os.environ.get('SECRET_KEY') or "secret string (can be as long as u want (actually it is mine so i dont care))"