from abc import ABC, abstractmethod


class ConfigurableAlgorithmBase(ABC):
    def __init__(self, algorithm):
        self.algorithm = algorithm

    @abstractmethod
    def __call__(self, function, bounds):
        pass

    @abstractmethod
    @property
    def __name__(self):
        pass
