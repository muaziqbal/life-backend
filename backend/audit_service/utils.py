import pymongo
from django.conf import settings
from datetime import datetime

client = pymongo.MongoClient(settings.MONGO_URI)
db = client[settings.MONGO_DB]
collection = db["logs"]

def log_action(user_id, action, metadata=None):
    entry = {
        "user_id": user_id,
        "action": action,
        "metadata": metadata or {},
        "timestamp": datetime.utcnow()
    }
    collection.insert_one(entry)
