from pydantic import PostgresDsn
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env"),
        case_sensitive=False,
        env_prefix="APP_CONFIG__",
    )

    # run
    host: str = "0.0.0.0"
    port: int = 8081

    # router
    api_prefix: str = "/api"

    # db
    db_url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


settings = Settings()
