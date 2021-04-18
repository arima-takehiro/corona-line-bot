from helper.logging import logging_config
from logic import data_getter, data_linker
from repository.datastore import DataStore

import logging


# GCFのエントリーポイント
def entry_point(event, context):
    logging_config()
    corona_data = data_getter.get_data()
    repo = DataStore()
    linker = data_linker.CoronaDataLinker(corona_data, repo=repo)
    linker.link()
