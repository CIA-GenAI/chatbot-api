from domain.DomainModel import DomainModel

class Healthcheck(DomainModel):
    cpu: int
    disc: int
    ram: int
    ok: bool
