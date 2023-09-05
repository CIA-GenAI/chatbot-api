import aioredis
from logging import Logger
from contextlib import asynccontextmanager
from collections.abc import AsyncGenerator
from app.config.database import RedisSettings


class CacheSession:

    def __init__(self, config: RedisSettings, logger: Logger) -> None:
        self._logger = logger
        self._config = config
        self._dsn: str = f"redis://{self._config.user}:*****@{self._config.host}/"
        self._client: aioredis.Redis = None

    @asynccontextmanager
    async def get(self) -> AsyncGenerator[aioredis.Redis]:
        
        if self._client is not None:
            yield self._client
            return

        self._logger.info(f"Connecting to cache database using dsn: {self._dsn}")
        dsn = self._dsn.replace("*****", self._config.pwd)

        try:
            self._client = aioredis.from_url(dsn, encoding="utf-8", decode_responses=True)
            yield self._client

        except:
            self._logger.info(f"Cannot connect to cache database: {self._dsn}")
            await self._client.close()
            self._client = None
