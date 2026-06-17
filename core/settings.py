from pydantic_settings import BaseSettings
from pathlib import Path
# Finds the root directory (Inventory_System) dynamically
ROOT_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    DATABASE_URL: str

    # class Config:
    #     env_file = str(ROOT_DIR / ".env")
        
    model_config = {
        "env_file": str(ROOT_DIR / ".env")
    }

settings = Settings()