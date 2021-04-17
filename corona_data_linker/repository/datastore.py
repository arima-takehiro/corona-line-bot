from google.cloud import datastore

import json
from typing import List
from datetime import date, datetime, timedelta
import logging

import sys
sys.path.append('./')
from helper.singleton import Singleton
from logic.interface.repository_interface import RepositoryInterface
from helper import config
from model.corona_data import CoronaData


class DataStore(RepositoryInterface, Singleton):

    c = config.Config()
    dclient = datastore.Client()
    logger = logging.getLogger('corona_data_linker_logger')


    def insert(self, corona_data: List[CoronaData]):
        today = date.today()
        c = config.Config
        batch = self.dclient.batch()
        batch.begin()

        for data in corona_data:
            key = self.dclient.key(str(today), data.pref_JP_name)
            entity = datastore.Entity(key)
            entity['pref_en_name'] = data.pref_EN_name
            entity['pref_jp_name'] = data.pref_JP_name
            entity['newly_confirmed'] = data.newly_confirmed
            entity['yesterday_confirmed'] = data.yesterday_confirmed
            entity['confirmed_by_city'] = data.confirmed_by_city
            entity['total_deaths'] = data.total_deaths
            entity['total_confirmed'] = data.total_confirmed
            entity['recovered'] = data.recovered
            batch.put(entity)

        batch.commit()
        self.logger.info("inserted today's data.")


    def delete(self, corona_data: List[CoronaData], data_period: int):
        target_day = date.today() - timedelta(days=data_period)

        batch = self.dclient.batch()
        batch.begin()

        for data in corona_data:
            key = self.dclient.key(str(target_day), data.pref_JP_name)
            batch.delete(key)

        batch.commit()
        self.logger.info("deleted {}'s data.".format(target_day))
