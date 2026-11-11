
from repositorio_pessoas import RepositorioPessoas


class RepositorioPessoasMemoria(RepositorioPessoas):

    def __init__(self):
        self.__pessoas = []

    def cadastrar(self, pessoa):
        self.__pessoas.append(pessoa)

    def buscar(self, nome):
        for pessoa in self.__pessoas:
            if pessoa.getNome() == nome:
                return pessoa
        return None

    def listar(self):
        return self.__pessoas

    def alterar(self, nome, nova_pessoa):
        pessoa = self.buscar(nome)

        if pessoa is None:
            return False

        indice = self.__pessoas.index(pessoa)
        self.__pessoas[indice] = nova_pessoa
        return True
