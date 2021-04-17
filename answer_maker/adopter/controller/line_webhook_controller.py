import sys
sys.path.append('../../')
from usecase.interfaces.make_answer_input_port import MakeAnswerInputPortInterface
from helper.config import Config
from adopter.controller.controller_interface import ControllerInterface


class LineWebhookController(ControllerInterface):
    def __init__(self, make_answer_input_port_interface: MakeAnswerInputPortInterface):
        self.make_answer_usecase = make_answer_input_port_interface

    def serve(self, body: str) -> str:
        self.make_answer_usecase.make_answer(body)


class MockController(ControllerInterface):
    def serve(self, body):
        return "pass"
