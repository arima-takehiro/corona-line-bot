from abc import ABCMeta
from abc import abstractmethod
from typing import List
from datetime import datetime


# The repository holding corona data must meet this interface.
class CoronaDataRepositoryInterface(metaclass=ABCMeta):
    @abstractmethod
    def get_by_pref(self, pref: str) -> str:
        """
        :param pref:
            取得したいデータの県名を取得する
        :return:
            CoronaのデータのJSONを返却する
        """
        pass
