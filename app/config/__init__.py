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
    'CLOUDINARY_CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME'),
    'CLOUDINARY_API_KEY': os.getenv('CLOUDINARY_API_KEY')
}


USER_SERVICE_URL = config['USER_SERVICE_HOST'] + ':' + config['USER_SERVICE_PORT']
TODO_SERVICE_URL = config['TODO_SERVICE_HOST'] + ':' + config['TODO_SERVICE_PORT']
