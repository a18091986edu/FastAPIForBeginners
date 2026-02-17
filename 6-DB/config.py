import os
from dotenv import load_dotenv
from pathlib import Path

# Загружаем переменные из .env файла
load_dotenv()

config_dir = Path(__file__).parent.parent.parent
dotenv_path = config_dir / ".env" / "DATABASE"
load_dotenv(dotenv_path)
print(dotenv_path)

# Database URL
DATABASE_URL = (
    f"postgresql+asyncpg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

# App settings
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
APP_NAME = os.getenv("APP_NAME", "FastAPI App")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")

# Проверка обязательных параметров в production
if not DEBUG and not os.getenv("DB_PASSWORD"):
    raise ValueError("DB_PASSWORD must be set in production")
