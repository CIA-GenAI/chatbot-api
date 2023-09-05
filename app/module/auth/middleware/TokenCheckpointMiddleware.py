from typing import Optional, Tuple
from starlette.requests import HTTPConnection
from starlette.authentication import AuthenticationBackend, AuthenticationError
from fastapi.security.utils import get_authorization_scheme_param
from app.module.auth.domain.dto.Token import Token
from app.module.auth.service.query.TokenQueryService import TokenQueryService

class TokenCheckpointMiddleware(AuthenticationBackend):

    def __init__(self, token_qs: TokenQueryService):
        self._token_qs = token_qs

    async def authenticate(
        self, conn: HTTPConnection
    ) -> Tuple[bool, Optional[Token]]:
        authorization: str = conn.headers.get("Authorization")
        if not authorization:
            return False, None

        scheme, token_str = get_authorization_scheme_param(authorization)
        if not (scheme and token_str):
            raise AuthenticationError("Not authenticated")

        if scheme.lower() != "bearer":
            raise AuthenticationError("Invalid authentication credentials")

        token = self._token_qs.check(token_str)

        if token is None:
            return False, None

        conn.scope["token"] = token

        return True, token
