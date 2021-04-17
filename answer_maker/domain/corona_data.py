from dataclasses import dataclass
from typing import List


@dataclass
class CoronaData(object):
    pref_EN_name: str
    pref_JP_name: str
    newly_confirmed: int
    yesterday_confirmed: int
    confirmed_by_city: List[str]
    deaths: int
    total_confirmed: int = 0
    recovered: int = 0
