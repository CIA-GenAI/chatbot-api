import logging
import logging.config
from os import path

from dependency_injector import containers, providers
from app.module.auth.middleware.TokenCheckpointMiddleware import TokenCheckpointMiddleware
from app.module.auth.repository.CredentialsRepository import CredentialsRepository
from app.module.auth.repository.TokenRepository import TokenRepository

from app.core.database.postgre import DatabaseSession
from app.core.database.mongo import DocumentSession
from app.core.database.weaviate import VectorSession
from app.core.database.redis import CacheSession
from app.core.database.sqlite import InMemorySession
from app.module.auth.service.query.TokenQueryService import TokenQueryService
from app.module.common.controller.ApiInfosController import ApiInfosController
from app.module.common.controller.HealthcheckController import HealthcheckController

from app.module.common.service.query.ApiInfosQueryService import ApiInfosQueryService
from app.module.common.service.query.HealthcheckQueryService import HealthcheckQueryService
from app.module.users.repository.UserRepository import UserRepository
from app.module.users.service.command.UserCommandService import UserCommandService
from app.module.users.service.query.UserQueryService import UserQueryService

from .settings import Settings

class Container(containers.DeclarativeContainer):

    config = Settings()

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
    
    apiinfos_qs = providers.Singleton(
        ApiInfosQueryService,
        config=config.api,
    )
    
    healthcheck_qs = providers.Singleton(
        HealthcheckQueryService
    )

    token_qs = providers.Singleton(
        TokenQueryService,
        token_repo=token_repo,
    )

    user_cs = providers.Singleton(
        UserCommandService,
        user_repo=user_repo,
    )
    
    user_qs = providers.Singleton(
        UserQueryService,
        user_repo=user_repo,
    )

    ########################################
    #       Register controllers           #
    ########################################
    
    apiinfos_ctr = providers.Singleton(
        ApiInfosController,
        apiinfos_qs=apiinfos_qs,
    )

    healthcheck_ctr = providers.Singleton(
        HealthcheckController,
        healthcheck_qs = healthcheck_qs
    )

    users_ctr = providers.Singleton(
        UserCommandService,
        user_cs=user_cs,
        user_qs=user_qs
    )

    #########################################
    # Register middlewares                  #
    #########################################
    token_mw = providers.Singleton(
        TokenCheckpointMiddleware,
        token_qs=token_qs
    )
    