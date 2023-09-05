from domain.DomainModel import DomainModel

class Helthcheck(DomainModel):
    cpu: int
    disc: int
    ram: int
    ok: bool
