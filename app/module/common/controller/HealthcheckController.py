from app.core.controller import BaseController
from app.module.common.domain.dto.Healthcheck import Healthcheck
from app.module.common.service.query.HealthcheckQueryService import HealthcheckQueryService
from app import get

class HealthcheckController(BaseController):

    def __init__(self, healthcheck_qs: HealthcheckQueryService) -> None:
        self._healthcheck_qs = healthcheck_qs
        pass


    @get("/healthcheck", response_model=Healthcheck)
    def get(self) -> Healthcheck:
        return self._healthcheck_qs.get()