"""Main constants of the project."""

from pathlib import Path

from pydantic_settings import BaseSettings

PROJECT_ROOT_PATH = Path(__file__).parents[1]


class Settings(BaseSettings):
    guest_list_path: Path = PROJECT_ROOT_PATH / "data" / "guest_list.csv"
