
import os
import mysql.connector
from dotenv import load_dotenv

from pessoa import Pessoa
from repositorio_pessoas import RepositorioPessoas

load_dotenv()


class RepositorioPessoasMySQL(RepositorioPessoas):

    def __init__(self):
        self.__host = os.getenv("MYSQL_HOST", "127.0.0.1")
        self.__port = int(os.getenv("MYSQL_PORT", "3307"))
        self.__usuario = os.getenv("MYSQL_USER", "root")
        self.__senha = os.getenv("MYSQL_PASSWORD")
        self.__banco = os.getenv("MYSQL_DATABASE", "cadastro")

        conexao = mysql.connector.connect(
            host=self.__host,
            port=self.__port,
            user=self.__usuario,
            password=self.__senha
        )

        cursor = conexao.cursor()
        cursor.execute(
            f"CREATE DATABASE IF NOT EXISTS `{self.__banco}`"
        )
        cursor.close()
        conexao.close()

        conexao = self.__conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pessoa (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                idade INT NOT NULL,
                email VARCHAR(255) NOT NULL
            )
        """)

        conexao.commit()
        cursor.close()
        conexao.close()

    def __conectar(self):
        return mysql.connector.connect(
            host=self.__host,
            port=self.__port,
            user=self.__usuario,
            password=self.__senha,
            database=self.__banco
        )

    def cadastrar(self, pessoa):
        conexao = self.__conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO pessoa (nome, idade, email) VALUES (%s, %s, %s)",
            (pessoa.getNome(), pessoa.getIdade(), pessoa.getEmail())
        )

        conexao.commit()
        cursor.close()
        conexao.close()

    def buscar(self, nome):
        conexao = self.__conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT nome, idade, email FROM pessoa WHERE nome = %s LIMIT 1",
            (nome,)
        )

        resultado = cursor.fetchone()

        cursor.close()
        conexao.close()

        if resultado is None:
            return None

        return Pessoa(resultado[0], resultado[1], resultado[2])

    def listar(self):
        conexao = self.__conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT nome, idade, email FROM pessoa ORDER BY id"
        )

        resultados = cursor.fetchall()

        cursor.close()
        conexao.close()

        return [
            Pessoa(nome, idade, email)
            for nome, idade, email in resultados
        ]

    def alterar(self, nome, nova_pessoa):
        conexao = self.__conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT id FROM pessoa WHERE nome = %s LIMIT 1",
            (nome,)
        )

        resultado = cursor.fetchone()

        if resultado is None:
            cursor.close()
            conexao.close()
            return False

        cursor.execute(
            """
            UPDATE pessoa
            SET nome = %s, idade = %s, email = %s
            WHERE id = %s
            """,
            (
                nova_pessoa.getNome(),
                nova_pessoa.getIdade(),
                nova_pessoa.getEmail(),
                resultado[0]
            )
        )

        conexao.commit()
        cursor.close()
        conexao.close()

        return True
