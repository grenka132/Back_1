from pydantic_settings import BaseSettings, SettingsConfigDict


class Setting(BaseSettings):
    model_config = SettingsConfigDict(
        extra='ignore',
        env_file='.env'
    )
    BASE_ROUTE_PATH: str

setting = Setting()