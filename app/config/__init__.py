import os
from dotenv import load_dotenv

load_dotenv()
config = {
    'SECRET_KEY': os.getenv('SECRET_KEY'),
    'REFRESH_TOKEN_SECRET_KEY': os.getenv('REFRESH_TOKEN_SECRET_KEY'),
    'USER_SERVICE_HOST': os.getenv('USER_SERVICE_HOST'),
    'USER_SERVICE_PORT': os.getenv('USER_SERVICE_PORT'),
    'TODO_SERVICE_HOST': os.getenv('TODO_SERVICE_HOST'),
    'TODO_SERVICE_PORT': os.getenv('TODO_SERVICE_PORT'),
}
