import json
import requests
from typing import List

import sys
sys.path.append('./')
from helper import config

from model import corona_data


def get_data() -> corona_data.CoronaData:
    """
    コロナのデータを取得して、モデルに入れて返す関数

    :return:
        corona_data.CoronaData：モデルに入れたコロナデータ
    """
    json_data = do_request()
    corona_data_list = convert_to_model(json_data)
    return corona_data_list


def do_request() -> dict:
    """
    リクエストを送信する関数

    :return:
        str：リクエストで取得したJson
    """
    c = config.Config()
    url = c.CORONA_URL

    response = requests.get(url)
    return response.json()


def convert_to_model(json_data: dict) -> List[corona_data.CoronaData]:
    """
    Dict型のデータから必要な情報だけをモデルに格納する関数

    :param dict_data:
        dict形式のデータ
    :return:
        List[corona_data.CoronaData]：モデルに格納されたコロナデータ
    """
    corona_data_list = []
    prefectures = json_data["prefectures"]
    for i in range(0, 51):
        pref = prefectures[i]
        cd = corona_data.CoronaData()
        cd.pref_JP_name = pref["name_ja"]
        cd.pref_EN_name = pref["name"]
        cd.newly_confirmed = pref["newlyConfirmed"]
        cd.yesterday_confirmed = pref["yesterdayConfirmed"]
        cd.confirmed_by_city = pref["confirmedByCity"]
        cd.total_deaths = pref["deaths"]
        cd.total_confirmed = pref["confirmed"]
        cd.recovered = pref["recovered"]
        corona_data_list.append(cd)

    return corona_data_list
