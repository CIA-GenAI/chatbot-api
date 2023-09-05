from pydantic import BaseModel

class ApiInfos(BaseModel):
    name: str
    description: str
    environment: str
    version: str
    debug: str
    key: str
    host: str
    port: str
    namespace: str