from bson import ObjectId
from pymongo.M import Model

class IntentSchema(Model):
    _id= ObjectId()
    tags: list[str] = []