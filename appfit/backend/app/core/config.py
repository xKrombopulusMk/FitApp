from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "sqlite:///./test.db"
    jwt_secret: str = "changeme"
    openai_api_key: str | None = None

    class Config:
        env_file = ".env"


settings = Settings()
