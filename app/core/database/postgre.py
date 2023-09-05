from contextlib import contextmanager, AbstractContextManager
from typing import Callable
from sqlalchemy import create_engine, orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from logging import Logger
from dependency_injector.providers import ConfigurationOption

Base = declarative_base()


class DatabaseSession:

    def __init__(self, config: ConfigurationOption, logger: Logger) -> None:
        self._logger = logger

        dsn: str = f"postgresql+psycopg2://{config.user}:*****@{config.host}:{config.port}/{config.db}"
        self._logger.info(f"Connecting to documents database using dsn: {dsn}")

        dsn.replace("*****", config.pwd)
        self._engine = create_engine(dsn, echo=True)

        self._factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
            ),
        )

    def create_database(self) -> None:
        Base.metadata.create_all(self._engine)

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        session: Session = self._factory()
        try:
            yield session
        except Exception:
            self._logger.exception("Session rollback because of exception")
            session.rollback()
            raise
        finally:
            session.close()