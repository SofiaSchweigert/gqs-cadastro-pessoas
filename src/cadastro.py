
"""Gerenciamento do cadastro de pessoas."""

from pessoa import Pessoa
from repositorio_pessoas_memoria import RepositorioPessoasMemoria


class CadastroPessoas:
    """Gerencia pessoas utilizando um repositorio."""

    def __init__(self, repositorio=None):
        if repositorio is None:
            repositorio = RepositorioPessoasMemoria()
        self.__repositorio = repositorio

    def cadastrar(self, nome, idade, email):
        pessoa = Pessoa(nome, idade, email)
        self.__repositorio.cadastrar(pessoa)
        return pessoa

    def buscarPorNome(self, nome):
        return self.__repositorio.buscar(nome)

    def listar(self):
        return self.__repositorio.listar()

    def alterar(self, nome, novo_nome, nova_idade, novo_email):
        nova_pessoa = Pessoa(novo_nome, nova_idade, novo_email)

        if self.__repositorio.alterar(nome, nova_pessoa):
            return nova_pessoa

        return None
