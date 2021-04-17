import sys
sys.path.append('./')
from adopter.controller.controller_interface import ControllerInterface


class Router():
    def __init__(self, controller_interface: ControllerInterface):
        self.controller = controller_interface

    def exec_router(self, body: str):
        self.controller.serve(body=body)
