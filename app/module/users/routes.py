from typing import List
from app.config.container import Container
from fastapi import FastAPI
from dependency_injector.wiring import inject, Provide
from dependency_injector.providers import Factory
from app.module.users.domain.model.User import User
from .controller.UserController import UserController

@inject
def load(app: FastAPI,
         controller: Factory[UserController] = Provide[Container.users_ctr]):
    
    @app.get("/users/all", response_model=List[User])
    def get_all():
        return controller.get_all()

    @app.get("/users/{id}", response_model=User)
    def get_by_id(id: int):
        return controller.get_by_id(id)