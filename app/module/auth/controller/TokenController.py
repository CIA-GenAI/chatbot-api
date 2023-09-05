from app.module.auth.domain.dto.Credentials import Credentials
from app.module.auth.domain.dto.Token import Token
from app.core.controller import BaseController
from app.module.auth.service.command.TokenCommandService import TokenCommandService
from app.module.auth.service.query.TokenQueryService import TokenQueryService


class TokenController(BaseController):

    def __init__(self,
                 token_cs: TokenCommandService,
                 token_qs: TokenQueryService) -> None:

        self._token_cs: TokenCommandService = token_cs
        self._token_qs: TokenQueryService = token_qs

    def create(self, credentials: Credentials):
        return self._token_cs.create(credentials)

    def check(self, token: str) -> Token | None:
        return self._token_qs.check(token)