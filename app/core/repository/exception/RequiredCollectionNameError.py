from ..AbstractRepository import T

class RequiredCollectionNameError(Exception):
    def __init__(self, model: T, id: str):
        super().__init__(f"{type(model)} not found, id: {id}")