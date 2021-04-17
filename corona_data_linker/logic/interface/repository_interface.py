from abc import ABCMeta, abstractmethod


class RepositoryInterface(metaclass=ABCMeta):
    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def delete(self, data_period):
        pass
