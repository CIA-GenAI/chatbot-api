from app.core.database.postgre import DatabaseSession
from app.module.users.domain.model.User import User
from app.core.repository.SQLRepository import SQLRepository


class UserRepository(SQLRepository[User]):
    def __init__(self, db_session: DatabaseSession) -> None:
        super().__init__(db_session)