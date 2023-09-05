from app.module.auth.domain.model.Credentials import Credentials

from app.module.auth.repository.CredentialsRepository import CredentialsRepository
from app.module.users.repository.UserRepository import UserRepository

class CredentialsCommandService:

    def __init__(self, credentials_repo: CredentialsRepository) -> None:
        self._credentials_repo: CredentialsRepository = credentials_repo

    def create(self, credentials: Credentials) -> bool:
        return self._credentials_repo.add(credentials)
