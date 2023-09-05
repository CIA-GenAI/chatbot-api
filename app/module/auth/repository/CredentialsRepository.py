from app.core.database.mongo import DocumentSession
from app.module.auth.domain.model.Credentials import Credentials
from app.module.auth.domain.model.Token import Token
from app.core.repository.DocumentRepository import DocumentRepository


class CredentialsRepository(DocumentRepository[Credentials]):
    def __init__(self, session: DocumentSession) -> None:
        super().__init__(session, Credentials.__name__)

    def create(self, credentials: Credentials) -> Token:
        return self.create(credentials)
    
    def credentials_exist(self, credentials: Credentials) -> bool:
        return self.get(credentials)
