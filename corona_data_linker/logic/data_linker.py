from injector import inject
from typing import List

import sys
sys.path.append('./')
from helper.config import Config
from .interface.repository_interface import RepositoryInterface
from model.corona_data import CoronaData

# repositoryに対して、新しいデータを更新・３日前のデータを削除します。
class CoronaDataLinker:
    def __init__(self, corona_data: List[CoronaData], repo: RepositoryInterface):
        self.corona_data = corona_data
        self.repo = repo

    def link(self):
        self._insert()
        self._delete()

    def _insert(self):
        self.repo.insert(self.corona_data)

    def _delete(self):
        c = Config()
        self.repo.delete(self.corona_data, data_period=c.DATA_PERIOD)
