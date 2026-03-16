from pydantic_settings import BaseSettings
from dotenv import load_dotenv


load_dotenv()

class Settings(BaseSettings):
    CHAT_ENDPOINT_URL: str = "http://127.0.0.1:8000/chat/answer"

    class Config:
        env_file = ".env"
        extra="allow"