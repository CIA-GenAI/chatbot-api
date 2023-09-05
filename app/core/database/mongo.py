from logging import Logger
from motor.motor_asyncio import AsyncIOMotorClient
from app.config.database import MongoDBSettings
from pymongo.database import Database

class DocumentSession:

    def __init__(self, config: MongoDBSettings, logger: Logger) -> None:
        self._logger = logger
        self._config = config

        dsn: str = f"mongodb+srv://{config.user}:{config.user}@{config.host}:{config.port}/{config.db}?retryWrites=true&w=majority"
        self._logger.info(f"Connecting to documents database using dsn")

        self._client = AsyncIOMotorClient(dsn)

    # ping server
    async def ping(self):
        try:
            self._client.admin.command('ping')
            return True
        except Exception:
            return False
        
    def get_db(self) -> Database:
        self._client.get_database(self._config.db)
