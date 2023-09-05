from pydantic import BaseModel

class Healthcheck(BaseModel):
    cpu: int
    disc: int
    ram: int
    ok: bool
