from pythondi import inject
from app.module.auth.domain.model.Credentials import Credentials
from app.module.auth.domain.model.Token import TokenModel
from app.module.auth.domain.model.Token import Token
from app.module.auth.helpers import create_access_token

from app.module.auth.repository.CredentialsRepository import CredentialsRepository
from app.module.auth.repository.TokenRepository import TokenRepository
from app.module.auth.repository.CredentialsRepository import CredentialsRepository
from app.module.auth.exception import CredentialsNotFoundException

class TokenCommandService:

    def __init__(self,
                 token_repository: TokenRepository,
                 credentials_repository: CredentialsRepository,
                 ttl: int) -> None:

        self._token_repo: TokenRepository = token_repository
        self._credentials_repo: CredentialsRepository = credentials_repository
        self._ttl = ttl
        

    def create(self, credentials: Credentials) -> Token:

        # check in db if the user credentials exists
        exist: bool = self._credentials_repo.credentials_exist(credentials)

        if not exist:
            raise CredentialsNotFoundException

        token: Token = create_access_token(
           credentials, ttl=self._ttl)

        return token

