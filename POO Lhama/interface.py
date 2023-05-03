from abc import ABC, abstractmethod


class AveVoadora(ABC):

    @abstractmethod
    def comer(self):
        raise 'Should Implement comer method'

    @abstractmethod
    def voar(self):
        raise 'Should Implement voar method'

    @abstractmethod
    def gritar(self):
        raise 'Should Implement gritar method'


class AveTerrestre(ABC):

    @abstractmethod
    def comer(self):
        raise 'Should Implement comer method'

    @abstractmethod
    def gritar(self):
        raise 'Should Implement gritar method'
