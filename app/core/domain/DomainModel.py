from typing import Annotated
from bson import ObjectId as _ObjectId
from pydantic import BaseModel, Field
from pydantic.functional_validators import AfterValidator


def check_object_id(value: str) -> str:
    if not _ObjectId.is_valid(value):
        raise ValueError('Invalid ObjectId')
    return value


ObjectId = Annotated[str, AfterValidator(check_object_id)]

class DomainModel(BaseModel):
    id: int | str | ObjectId = Field(None, description="ID")

    class Config:
        from_attributes = True
