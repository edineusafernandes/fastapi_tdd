from paydantic_settings import BaseSettinggs

class Settings(BaseSettings):
    PROJECT_NAME: str = "Story API"
    ROOT_PATH: str = "/"

    DATABASE_URL: str 


    model_config = SettingsConfigDict(env_file="env")

    settings = Settings()

