from contextlib import asynccontextmanager
from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from logging import Logger
from app.config.database import PostgreDBSettings
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import sessionmaker
from concurrent.futures import ThreadPoolExecutor
from sqlalchemy.schema import MetaData

Base = declarative_base()


class DatabaseSession:

    def __init__(self, config: PostgreDBSettings, logger: Logger, metadata: MetaData) -> None:
        self._logger: Logger = logger
        self._config: PostgreDBSettings = config
        self._metadata: MetaData = metadata
        self._engine: AsyncEngine = None
        self._session: AsyncSession = None
        self._initialized: bool = False
        self._dsn: str = f"postgresql+asyncpg://{config.user}:*****@{config.host}:{config.port}/{config.db}"


    async def initialize(self) -> None:
        async with self.connect() as engine:
            async with engine.begin() as conn:
                try:
                    self._logger.info(f"Initializing database")
                    await conn.run_async(lambda: self._metadata.create_all())
                    self._initialized = True
                except:
                    self._logger.error(f"Failed initializing database: {self._dsn}")
                    self._initialized = False 


    @asynccontextmanager 
    async def get(self) -> AsyncGenerator[AsyncSession]:

        if self._initialized is False:
            await self.initialize()

        async with self.connect() as engine:
            async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

            async with async_session() as session:
                self._session = session
                yield session


    @asynccontextmanager     
    async def connect(self) -> AsyncGenerator[AsyncEngine]:

        if self._engine is not None:
            yield self._engine

        self._logger.info(f"Connecting to database using dsn: {self._dsn}")
        dsn = self._dsn.replace("*****", self._config.pwd)

        try:
            self._engine = create_async_engine(dsn, echo=True, poolclass=ThreadPoolExecutor)
            yield self._client

        except:
            self._logger.error(f"Failed connecting to the database: {self._dsn}")
            await self._engine.dispose()
            self._client = None
