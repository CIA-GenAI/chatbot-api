
from fastapi import FastAPI
from fastapi.openapi import utils
from fastapi.middleware.cors import CORSMiddleware
from .config.container import Container

from .module.auth.middleware.AuthenticationMiddleware import AuthenticationMiddleware
from .module.auth.middleware.TokenCheckpointMiddleware import TokenCheckpointMiddleware

from .module.users import routes as usersRoutes
from .module.common import routes as commonRoutes

from .config.settings import Settings

config = Settings()

def bootstrap() -> FastAPI:

    app = FastAPI()

    container = Container()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=['http://localhost'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
    
    app.add_middleware(
        AuthenticationMiddleware,
        backend=container.token_mw()
    )

    @app.on_event('startup')
    async def startup():
        container.logger().info(f"Application is starting ...")
        container.token_mw()
        
    @app.on_event("shutdown")
    async def shutdown_event():
        container.logger().error(f"Application is shutting down ...")

    # usersRoutes.load(app)
    commonRoutes.load(app)

    app.openapi_schema = utils.get_openapi(
        title = config.openapi.title,
        version = config.openapi.version,
        description = config.openapi.description,
        routes = app.routes 
    )

    return app
