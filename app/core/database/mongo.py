import motor.motor_asyncio


from logging import Logger
from dependency_injector.providers import ConfigurationOption

class DocumentSession:

    def __init__(self, config: ConfigurationOption, logger: Logger) -> None:
        self._logger = logger

        dsn: str = f"mongodb+srv://{config.user}:*****@{config.host}:{config.port}/{config.db}?retryWrites=true&w=majority"
        self._logger.info(f"Connecting to documents database using dsn: {dsn}")

        dsn.replace("*****", config.pwd)
        self.client = motor.motor_asyncio.AsyncIOMotorClient(dsn)
