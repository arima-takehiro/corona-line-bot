from abc import ABCMeta, abstractmethod


class ControllerInterface(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, body: str):
        pass
