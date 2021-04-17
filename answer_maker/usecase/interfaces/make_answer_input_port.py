from abc import ABCMeta
from abc import abstractmethod


# MakeAnswerInputPortInterfaceはユースケースの Interactor が満たすべきインターフェースです。
class MakeAnswerInputPortInterface(metaclass=ABCMeta):
    @abstractmethod
    def make_answer(self):
        pass
