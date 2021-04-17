from dataclasses import dataclass
import os

from .singleton import Singleton


class Config(Singleton):
    PROJECT_ID = os.getenv("PROJECT_ID")

    DATA_PERIOD = 2
    CORONA_URL = "https://raw.githubusercontent.com/reustle/covid19japan-data/master/docs/summary/latest.json"
