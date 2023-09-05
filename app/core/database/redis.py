import aioredis

from logging import Logger
from dependency_injector.providers import ConfigurationOption

class CacheSession:

    async def __init__(self, config: ConfigurationOption, logger: Logger) -> None:
        self._logger = logger

        dsn: str = f"redis://{config.user}:*****@{config.host}/"
        self._logger.info(f"Connecting to cache database using dsn: {dsn}")

        dsn.replace("*****", config.pwd)
        self.client = await aioredis.from_url(dsn, decode_responses=True)
