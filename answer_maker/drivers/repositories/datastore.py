from datetime import date
from typing import List

from google.cloud import datastore
from jp_pref import prefecture

import sys
sys.path.append("../")
from usecase.interfaces import corona_data_repository
from helper import config


class DatastoreRepository(corona_data_repository.CoronaDataRepositoryInterface):
    c = config.Config()
    dclient = datastore.Client()

    def __init__(self):
        pass

    def get_by_pref(self, pref: str) -> str:
        """
        TODO:
            get covid data by pref name
        """
        today = date.today()
        query = self.dclient.query(kind=str(today))
        query = query.add_filter("pref_jp_name", '=', pref)
        result = query.fetch(1)
        result = list(result)
        print("get the {}'s data.".format(result[0]["pref_en_name"]))
        return result[0]
