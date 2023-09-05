from app.module.auth.domain.dto.Credentials import Credentials
from app.module.auth.domain.dto.Token import Token
from app.core.controller import BaseController
from app.module.auth.service.command.TokenCommandService import TokenCommandService
from app.module.auth.service.query.TokenQueryService import TokenQueryService


class HealthcheckController(BaseController):

    def __init__(self) -> None:
        pass