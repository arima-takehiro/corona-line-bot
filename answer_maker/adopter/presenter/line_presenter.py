import datetime

from linebot import (
    LineBotApi,
    WebhookHandler
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

import sys
sys.path.append('../../')
from domain import corona_data
from helper import config


class LinePresenter:
    """
    LinePresenter is the presenter that output message to LINE bot.
    """

    c = config.Config()

    def __init__(self):
        pass


    def out(self, corona_data: str, errMsg: str):
        formatted_message = self._create_message(corona_data, errMsg)
        self._send_message(formatted_message)


    line_bot_api = LineBotApi(c.LINE_ACCESS_TOKEN)
    handler = WebhookHandler(c.LINE_CHANNEL_SECRET)


    @handler.add(MessageEvent, message=TextMessage)
    def _send_message(self, formatted_message):
        self.line_bot_api.reply_message(
            self.c.REPLY_TOKEN,
            TextSendMessage(text=formatted_message)
        )


    def _create_message(self, data: corona_data.CoronaData, errMsg: str) -> str:
        """
        create_message format the message into the format you want to output to LINE bot.

        :param data:
            data is data resource.
        :return:
            message formatted
        """
        if errMsg == "":

            with open("adopter/presenter/output_template.txt") as f:
                return f.read().format(
                    today=datetime.date.today().__str__(),
                    jp_pref_name=data.pref_JP_name,
                    total_confirmed=data.total_confirmed,
                    newly_confirmed=data.newly_confirmed,
                    yesterday_confirmed=data.yesterday_confirmed,
                    recovered=data.recovered,
                    deaths=data.deaths,
                    confirmed_by_city=self.create_confirmed_by_city_message(data)
                ).__str__()

        else:
            with open("adopter/presenter/error_template.txt") as f:
                return f.read().__str__()


    def create_confirmed_by_city_message(self, data: corona_data.CoronaData) -> str:
        res = ""
        print(data.confirmed_by_city)
        for k, v in data.confirmed_by_city.items():
            res += "{}: {}\n".format(k, v)

        return res



