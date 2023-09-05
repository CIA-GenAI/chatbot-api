import logging
import logging.config
from os import path

from dependency_injector import containers, providers
from app.module.auth.repository.CredentialsRepository import CredentialsRepository
from app.module.auth.repository.TokenRepository import TokenRepository

from app.core.database.postgre import DatabaseSession
from app.core.database.mongo import DocumentSession
from app.core.database.weaviate import VectorSession
from app.core.database.redis import CacheSession
from app.core.database.sqlite import InMemorySession

from app.module.users.repository.UserRepository import UserRepository
from app.module.users.service.command.UserCommandService import UserCommandService
from app.module.users.service.query.UserQueryService import UserQueryService

from .settings import Settings

class Container(containers.DeclarativeContainer):

    config = providers.Configuration(
        pydantic_settings=[Settings()], strict=True)

    # Register the logger
    conf_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
    logging.config.fileConfig(conf_path, disable_existing_loggers=False)
    logger = providers.Resource(
        logging.getLogger,
        name=config.api.namespace,
    )

    ##########################################
    #       Register Database Sessions        #
    ##########################################
    db = providers.Singleton(DatabaseSession,
        config=config.database.postgre, logger=logger)
    
    document = providers.Singleton(DocumentSession,
        config=config.database.mongo, logger=logger)

    vector = providers.Singleton(VectorSession,
        config=config.database.weaviate, logger=logger)
    
    cache = providers.Singleton(CacheSession,
        config=config.database.redis, logger=logger)

    memory = providers.Singleton(InMemorySession,
        config=config.database.sqlite, logger=logger)


    # ######################################
    #         Register Repositories        #
    # ######################################
    credentials_repo = providers.Singleton(
        CredentialsRepository,
        session=document,
    )
    token_repo = providers.Singleton(
        TokenRepository,
        session=cache,
    )
    user_repo = providers.Factory(
        UserRepository,
        session=db,
    )
    
    # ######################################
    #         Register Services            #
    # ######################################
    
    user_command_service = providers.Factory(
        UserCommandService,
        user_repo=user_repo,
    )
    
    user_query_service = providers.Factory(
        UserQueryService,
        user_repo=user_repo,
    )

    ########################################
    #       Register controllers           #
    ########################################
    users_controller = providers.Factory(
        UserCommandService,
        user_cs=user_command_service,
        user_qs=user_query_service
    )
