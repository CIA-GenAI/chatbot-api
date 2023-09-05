from app.module.common.domain.dto.Healthcheck import Healthcheck
from fastapi import FastAPI

def load(app: FastAPI):

    @app.post("/healthcheck", response_model=Healthcheck)
    def get():
        return Healthcheck(
            cpu = 0,
            disc = 0,
            ram = 0,
            ok = True
        )
