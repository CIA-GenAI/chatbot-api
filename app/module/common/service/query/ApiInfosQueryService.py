
from app.config.api import APISettings


class ApiInfosQueryService:

    def __init__(self, config: APISettings) -> None:
        self._config = config
    
    def get(self) -> APISettings:
        return self._config
