from typing import List
from app.config.container import Container
from fastapi import FastAPI
from dependency_injector.wiring import inject, Provide
from dependency_injector.providers import Factory
from app.module.users.domain.model.User import User
from .controller.TokenController import TokenController
from .domain.model.Token import Token
from .domain.dto.Credentials import Credentials

@inject
def load(app: FastAPI,
         controller: Factory[TokenController] = Provide[Container.token_controller]):

    @app.post("/auth/token", response_model=Token)
    def create(credentials: Credentials):
        return controller.create(credentials)

    @app.get("/auth/token/check/{token}", response_model=Token)
    def get(token: str):
        return controller.check(token)