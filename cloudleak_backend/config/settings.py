import os

from dotenv import load_dotenv

load_dotenv()


class CeleryConfig:
    REDIS_BROKER_URL = os.getenv("REDIS_BROKER_URL", "redis://localhost:6379/0")
    REDIS_BACKEND_URL = os.getenv("REDIS_BACKEND_URL", "redis://localhost:6379/0")
    CELERY_CONFIG = {
        "broker_url": REDIS_BROKER_URL,
        "result_backed": REDIS_BACKEND_URL,
        "task_serializer": "pickle",
        "result_serializer": "pickle",
        "accept_content": ["pickle"],
        "result_accept_content": ["pickle"],
        "task_max_retries": None,
        "include": [],
    }

class MongoConfig:
    MONGO_USERNAME = os.getenv("MONGO_USERNAME")
    MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
    MONGO_PORT = os.getenv("MONGO_PORT", 27017)
    MONGO_URI = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@mongo:27017/cloudleak?authSource=admin"
