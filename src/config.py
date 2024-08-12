from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # app
    host: str = "0.0.0.0"
    port: int = 8080

    # router
    api_prefix: str = "/api"


settings = Settings()
