import uvicorn
import asyncio
from fastapi import FastAPI
from .decorator import singleton
from functools import wraps
from ..config.settings import Settings
from fastapi.openapi import utils
from fastapi.middleware.cors import CORSMiddleware
from ..module.auth.middleware.AuthenticationMiddleware import AuthenticationMiddleware
from ..module.auth.middleware.TokenCheckpointMiddleware import TokenCheckpointMiddleware
from typing import TypeVar


@singleton
class Application(FastAPI):


    def __init__(self) -> None:
        super().__init__()
        self._config = Settings()


    def bootstrap(self) -> None:

        from ..config.container import Container

        container = Container()

        self.add_middleware(
            CORSMiddleware,
            allow_origins=['http://localhost'],
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*'])
        
        self.add_middleware(
            AuthenticationMiddleware,
            backend=container.token_mw())

        @self.on_event('startup')
        async def startup():
            container.logger().info(f"Application is starting ...")
            container.token_mw()
            
        @self.on_event("shutdown")
        async def shutdown_event():
            container.logger().error(f"Application is shutting down ...")


        container.openapi_schema = utils.get_openapi(
            title = self._config.openapi.title,
            version = self._config.openapi.version,
            description = self._config.openapi.description,
            routes = self.routes)


    def route(self):

        T = TypeVar("T")

        def get(path: str, response_model: T) -> T:
            @self.get(path, response_model=response_model)
            def decorator_get(func) -> T:
                @wraps(func)
                def wrapper_get(*args, **kwargs) -> T:
                    return func(*args, **kwargs)
                return wrapper_get
            return decorator_get


        def post(path: str, response_model: T) -> T:
            @self.post(path, response_model=response_model)
            def decorator_post(func) -> T:
                @wraps(func)
                def wrapper_post(*args, **kwargs) -> T:
                    return func(*args, **kwargs)
                return wrapper_post
            return decorator_post


        def put(path: str, response_model: T) -> T:
            @self.put(path, response_model=response_model)
            def decorator_put(func) -> T:
                @wraps(func)
                def wrapper_put(*args, **kwargs) -> T:
                    return func(*args, **kwargs)
                return wrapper_put
            return decorator_put


        def delete(path: str, response_model: T) -> T:
            @self.delete(path, response_model=response_model)
            def decorator_delete(func) -> T:
                @wraps(func)
                def wrapper_delete(*args, **kwargs) -> T:
                    return func(*args, **kwargs)
                return wrapper_delete
            return decorator_delete


        return get, post, put, delete


    async def run(self) -> None:

        config = uvicorn.Config(
            "main:app",
            host = self._config.api.host,
            port = int(self._config.api.port),
            reload = self._config.api.debug)

        server = uvicorn.Server(config)

        await server.serve()
