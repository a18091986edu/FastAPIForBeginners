from pathlib import Path
from dotenv import load_dotenv
from dataclasses import dataclass, field
import os

config_dir = Path(__file__)  # .parent.parent.parent
dotenv_path = config_dir / ".env"

load_dotenv()


@dataclass
class DataBaseConfig:
    connection_string: str
    user: str
    password: str
    host: str
    database: str
    port: int = field(default=5432)

    def __post_init__(self):
        self.url = f"{self.connection_string}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


@dataclass
class Config:
    main_db: DataBaseConfig
    slave_db: DataBaseConfig


def init_config():
    main_db = DataBaseConfig(
        connection_string=os.getenv("DB_CONNECTION_STRING"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
    )
    slave_db = DataBaseConfig(
        connection_string=os.getenv("DB_SLAVE_CONNECTION_STRING"),
        user=os.getenv("DB_SLAVE_USER"),
        password=os.getenv("DB_SLAVE_PASSWORD"),
        host=os.getenv("DB_SLAVE_HOST"),
        port=os.getenv("DB_SLAVE_PORT"),
        database=os.getenv("DB_SLAVE_NAME"),
    )

    return Config(main_db=main_db, slave_db=slave_db)


config = init_config()


if __name__ == "__main__":
    init_config()
    print(config.main_db.url)
