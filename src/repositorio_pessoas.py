
from abc import ABC, abstractmethod


class RepositorioPessoas(ABC):

    @abstractmethod
    def cadastrar(self, pessoa):
        pass

    @abstractmethod
    def buscar(self, nome):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def alterar(self, nome, nova_pessoa):
        pass
