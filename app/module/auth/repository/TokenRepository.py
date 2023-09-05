from app.core.database.redis import CacheSession
from app.module.auth.domain.model.Credentials import Credentials
from app.module.auth.domain.model.Token import Token
from app.core.repository.CacheRepository import CacheRepository
from app.module.auth.helpers import get_token_id


class TokenRepository(CacheRepository[Token]):
    def __init__(self, session: CacheSession) -> None:
        super().__init__(session)

    def create(self, credentials: Credentials) -> Token:
        return self.create(credentials)

    def check(self, token: str) -> Token | None:
        id: str = get_token_id(token)
        return self.get_by_id(id)
