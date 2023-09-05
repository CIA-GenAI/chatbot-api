from app.module.auth.domain.dto.Token import Token
from app.module.auth.repository.TokenRepository import TokenRepository

class TokenQueryService:

    def __init__(self, token_repo: TokenRepository) -> None:
        self._token_repo: TokenRepository = token_repo

    def check(self, token: str) -> Token | None:
        record = self._token_repo.check(token)
        return Token(**record) if record is not None else None
