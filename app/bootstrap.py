import uvicorn

from fastapi import FastAPI
from fastapi.openapi import utils
from fastapi.middleware.cors import CORSMiddleware

from .config.container import Container

from .module.auth.middleware.AuthenticationMiddleware import AuthenticationMiddleware
from .module.auth.middleware.TokenCheckpointMiddleware import TokenCheckpointMiddleware

from .module.users import routes as usersRoutes
from .module.common import routes as commonRoutes



def bootstrap(container: Container):

    app = FastAPI()

    app.openapi_schema = utils.get_openapi(
        title = container.config.openapi.title,
        version = container.config.openapi.version,
        description = container.config.openapi.description,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=['http://localhost'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )

    @app.on_event('startup')
    async def startup():
        app.add_middleware(AuthenticationMiddleware,
                           backend=TokenCheckpointMiddleware())
        container.logger.error(f"Application is starting ...")


    @app.on_event("shutdown")
    async def shutdown_event():
        container.logger.error(f"Application is shutting down ...")
    


def load_routes(app: FastAPI):
    usersRoutes.load(app)
    commonRoutes.load(app)

def run():
    container = Container()
    bootstrap(container)

    # launch unicorn server
    uvicorn.run(
        "main:app",
        host=container.config.api.host,
        reload=container.config.api.debug,
        port=container.config.api.port,
    )