from datetime import datetime

from jp_pref import prefecture

import sys
sys.path.append('../../')
from usecase.interfaces.corona_data_repository import CoronaDataRepositoryInterface
from usecase.interfaces.make_answer_presenter import MakeAnswerPresenterInterface
from usecase.interfaces.make_answer_input_port import MakeAnswerInputPortInterface
from domain import corona_data


class MakeAnswerUseCase(MakeAnswerInputPortInterface):
    def __init__(self, repo: CoronaDataRepositoryInterface, presenter: MakeAnswerPresenterInterface):
        """

        :param repo:
            repo is the repository holding corona data.
        :param presenter:
            presenter is the output.
        """
        self.repo = repo
        self.presenter = presenter


    def make_answer(self, message: str):
        try:
            prefecture.name2code(message)
        except KeyError as errmsg:
            print("User input 「{}」 is invalid. Please input prefecture name.".format(message))
            self.presenter.out("", errmsg)

        corona_data = self.get_corona_data(message)
        self.presenter.out(corona_data, "")


    def get_corona_data(self, pref: str) -> corona_data.CoronaData:
        """
        get corona data by specifing prefecture name

        :param pref:
            pref is prefecture name that you wanna get data
        :param repo:
            repo is the repository holding corona data.
        :return:
        """
        pref = self.convert_to_pref_name(pref)
        query_res = self.repo.get_by_pref(pref)
        return self.convert_to_corona_model(query_res)


    def convert_to_pref_name(self, pref: str) -> str:
        """
        This function is that convert prefecture name to long one.
        ex:
        東京 -> 東京都
        福岡 -> 福岡県

        If the pref received as an argument is a long one, return it as is.
        ex:
        福岡県 -> 福岡県

        :param pref:
        :return:
        """
        pref_code = prefecture.name2code(pref)
        pref_long_name = prefecture.code2name(pref_code)
        return pref_long_name


    def convert_to_corona_model(self, query_res) -> corona_data.CoronaData:
        """
        This function is that convert to CoronaData model.

        :param query_res:
        :return:
        """
        cd = corona_data.CoronaData(
            deaths = query_res["total_deaths"],
            yesterday_confirmed=query_res["yesterday_confirmed"],
            pref_EN_name=query_res["pref_en_name"],
            pref_JP_name=query_res["pref_jp_name"],
            newly_confirmed=query_res["newly_confirmed"],
            confirmed_by_city=query_res["confirmed_by_city"],
            total_confirmed=query_res["total_confirmed"],
            recovered=query_res["recovered"],
        )
        return cd
