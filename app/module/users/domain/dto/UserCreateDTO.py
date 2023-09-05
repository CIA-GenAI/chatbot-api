from pydantic import BaseModel, EmailStr, constr

class UserCreateUserDTO(BaseModel):
    fullname: str
    email: EmailStr
    password: constr(min_length=8)
    passwordConfirm: str
