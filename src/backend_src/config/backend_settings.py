from pydantic_settings import BaseSettings
from dotenv import load_dotenv


load_dotenv()

class Settings(BaseSettings):
    API_HOST: str = "localhost"
    API_PORT: int = 8000

    class Config:
        env_file = ".env"
        extra="allow"