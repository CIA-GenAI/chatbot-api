from __future__ import annotations
from app.core.controller import BaseController
from app.module.common.domain.dto.ApiInfos import ApiInfos
from app.module.common.service.query.ApiInfosQueryService import ApiInfosQueryService
from app import get


class ApiInfosController(BaseController):

    def __init__(self, apiinfos_qs: ApiInfosQueryService) -> None:
        self._apiinfos_qs = apiinfos_qs

    @get("/", response_model=ApiInfos)
    def get(self) -> ApiInfos:
        return ApiInfos(**self._apiinfos_qs.get())
