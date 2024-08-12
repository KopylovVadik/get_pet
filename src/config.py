from pydantic_settings import BaseSettings
from pydantic import PostgresDsn


class Settings(BaseSettings):
    # app
    host: str = "0.0.0.0"
    port: int = 8080

    # router
    api_prefix: str = "/api"

    # db
    db_url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


settings = Settings()
