from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    aws_secret_access_key: str
    aws_secret_access_key_id: str
    region_name: str

    model_config = SettingsConfigDict(env_file=".env")
