# project/app/config.py


import logging
from functools import lru_cache

from pydantic_settings import BaseSettings
from pydantic import AnyUrl


log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = 0
    database_url: AnyUrl = None


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()