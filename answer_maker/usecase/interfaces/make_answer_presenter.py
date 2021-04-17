from abc import abstractmethod
from abc import ABCMeta


# AnswerOutputPortInterfaceはデータの出力先クラスが満たすべきインターフェースです。
class MakeAnswerPresenterInterface(metaclass=ABCMeta):
    @abstractmethod
    def out(self, corona_data: str, message_valid: bool):
        pass
