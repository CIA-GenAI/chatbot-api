from pydantic import constr

from app.core.domain.DomainModel import DomainModel, ObjectId

class Credentials(DomainModel):
    username: constr(min_length=100)
    password: constr(min_length=8)
    user_id: ObjectId
