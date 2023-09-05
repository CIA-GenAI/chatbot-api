from app.core.domain.DomainModel import DomainModel

class Token(DomainModel):
    access_token: str
    token_type: str
    expiry_date: str