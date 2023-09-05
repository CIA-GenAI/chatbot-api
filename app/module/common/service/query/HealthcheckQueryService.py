
from app.module.common.domain.dto.Healthcheck import Healthcheck

class HealthcheckQueryService:

    def get() -> Healthcheck:

        # these values should be computed
        return Healthcheck(
            cpu = 0,
            disc = 0,
            ram = 0,
            ok = True
        )

