import weaviate
from logging import Logger
from dependency_injector.providers import ConfigurationOption

class VectorSession:

    def __init__(self, config: ConfigurationOption, logger: Logger) -> None:
        self._logger = logger
        
        auth_config = weaviate.auth.AuthApiKey(
            api_key=config.api_key)

        self._engine = weaviate.Client(
            url=config.url,
            auth_client_secret=auth_config,
            additional_headers={
                "X-Cohere-Api-Key": config.cohere_api_key,
            }
        )
