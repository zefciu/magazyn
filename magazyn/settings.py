from functools import lru_cache
from os import environ
from typing import Annotated

from fastapi import Depends
from pydantic import BaseModel
from yaml import safe_load


CONFIG_FILE_NAME = environ.get("CONFIG_FILE", "config.yaml")


class SettingsModel(BaseModel):
    """Main application settings class"""

    db_url: str


@lru_cache
def get_settings() -> SettingsModel:
    with open(CONFIG_FILE_NAME, "r") as f:
        data = f.read()
    return SettingsModel.model_validate(safe_load(data))


Settings = Annotated[SettingsModel, Depends(get_settings)]
