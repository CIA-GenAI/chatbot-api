from bson.objectid import ObjectId
from pydantic import BaseModel, Field
from typing import Generic, TypeVar
from .DomainModel import DomainModel

D = TypeVar("D", bound=DomainModel)

class DomainObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, ObjectId):
            raise TypeError('ObjectId required')
        return str(v)


class DocumentModel(Generic[D]):
    # _id: DomainObjectId = Field(None, description="ID")
    pass
