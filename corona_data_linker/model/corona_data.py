import dataclasses
from typing import List


@dataclasses.dataclass
class CoronaData:
    pref_EN_name: str = ""
    pref_JP_name: str = ""
    newly_confirmed: int = 0
    yesterday_confirmed: int = 0
    confirmed_by_city: List[str] = dataclasses.field(default_factory=list)
    total_deaths: int = 0
    total_confirmed: int = 0
    recovered: int = 0
