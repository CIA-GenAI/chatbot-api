from fastapi import FastAPI

from app.config.container import Container
from dependency_injector.wiring import inject, Provide
from dependency_injector.providers import Singleton

from app.module.common.controller.ApiInfosController import ApiInfosController
from app.module.common.controller.HealthcheckController import HealthcheckController

from app.module.users.domain.model.User import User
from app.module.common.domain.dto.Healthcheck import Healthcheck
from app.module.common.domain.dto.ApiInfos import ApiInfos


@inject
def load(app: FastAPI,
         apiinfos_ctr: Singleton[ApiInfosController] = Provide[Container.apiinfos_ctr],
         healthcheck_ctr: Singleton[HealthcheckController] = Provide[Container.healthcheck_ctr]):

    @app.post("/", response_model=ApiInfos)
    def get_api_infos():
        return apiinfos_ctr.get()

    @app.post("/healthcheck", response_model=Healthcheck)
    def get_healthcheck():
        return healthcheck_ctr.get()
