from pydantic import constr

from app.core.domain import DocumentModel

class Credentials(DocumentModel):
    username: constr(min_length=100)
    password: constr(min_length=8)
    user_id: str
