from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL: str = Field(default='postgresql+asyncpg://dio_fastapi_user:dio_fastapi@localhost:5432/dio_fastapi_db')

settings = Settings()