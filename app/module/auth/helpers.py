from jose import JWTError, jwt
from datetime import datetime, timedelta
from app.module.auth.domain.dto.Credentials import Credentials
from app.module.auth.domain.model.Token import Token

def create_access_token(
    credentials: Credentials,
    ttl: int,
    secret: str,
    algorithm: str) -> Token:

    expiry_date = datetime.utcnow() + timedelta(minutes=ttl)
    access_token = jwt.encode(credentials, key=secret, algorithm=algorithm)

    return Token(
        access_token=access_token,
        token_type="bearer",
        expiry_date=expiry_date)


def get_token_id(credentials: Credentials) -> str:
    return f"token-{credentials.username}"

def get_token_id(token: str) -> str:
    credentials: Credentials = decode_token(token)
    return get_token_id(credentials)

def decode_token(token: str) -> Credentials:
    try:
        data = jwt.decode(token)
        return data
    except JWTError as e:
        raise e
    
