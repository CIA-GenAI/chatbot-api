import time
from fastapi import FastAPI, Request


class SampleMiddleware:
    # inject fastapi app here
    app: FastAPI

    def __init__(self, app: FastAPI) -> None:
        self.app = app

    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        return response