from ..AbstractRepository import T

class DocumentDomainRequiredError(TypeError):
    def __init__(self, model: T):
        super().__init__(f"Document Domain Object expected, {type(model)} provided.")