from pydantic import BaseModel, Field
from pydantic import constr

class Credentials(BaseModel):
    username: constr(min_length=100)
    password: constr(min_length=8)
