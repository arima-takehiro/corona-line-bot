import logging

from flask import Flask, request
from linebot import (
    LineBotApi,
    WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage
)

from helper import logging
from helper import router
from helper.config import Config
from adopter.controller import controller_interface
from adopter.controller.line_webhook_controller import LineWebhookController
from usecase.interfaces.make_answer_input_port import MakeAnswerInputPortInterface
from usecase.interfaces.make_answer_presenter import MakeAnswerPresenterInterface
from usecase.interfaces.corona_data_repository import CoronaDataRepositoryInterface
from usecase.impl.make_answer_usecase import MakeAnswerUseCase
from drivers.repositories.datastore import DatastoreRepository
from adopter.presenter.line_presenter import LinePresenter
from adopter.controller.controller_interface import ControllerInterface


app = Flask(__name__)

c = Config()
line_bot_api = LineBotApi(c.LINE_ACCESS_TOKEN)
handler = WebhookHandler(c.LINE_CHANNEL_SECRET)


@app.route("/callback", methods=['POST'])
def callback():
    """
    This function is LINE health check handler.
    """
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    """
    This function is LINE webhook handler.
    """
    logging.logging_config()
    c.REPLY_TOKEN = event.reply_token
    r = di()
    r.exec_router(event.message.text)

# いずれはDIライブラリを使いたい。pinject, flask-injector, injectorを試したが、うまくいかなかった。
def di():
    lp = LinePresenter()
    repo = DatastoreRepository()
    uc = MakeAnswerUseCase(repo, lp)
    lwc = LineWebhookController(uc)
    r = router.Router(lwc)
    return r


if __name__ == "__main__":
    app.run(debug=c.DEBUG)
