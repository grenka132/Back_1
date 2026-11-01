from pydantic_settings import BaseSettings, SettingsConfigDict


class Setting(BaseSettings):
    model_config = SettingsConfigDict(
        extra='ignore',
        env_file='.env'
    )
    BASE_ROUTE_PATH: str = "/api/v1"
    SAVE_FILE: str = "saves/save.json"
    SQLALCHEMY_DATABASE_URL: str = "postgresql+asyncpg://user:password@localhost:5432/Save_DB"

setting = Setting()