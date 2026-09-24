# Sistema de Cadastro de Pessoas - versao 2
# novos requisitos: menu, consulta, alteracao e listagem
"""Sistema de cadastro de pessoas."""


def exibir_menu():
    """Exibe o menu principal."""
    print("=========================")
    print(" CADASTRO DE PESSOAS")
    print("=========================")
    print("1 - Cadastrar pessoa")
    print("2 - Consultar pessoa")
    print("3 - Alterar pessoa")
    print("4 - Listar pessoas")
    print("5 - Avalisar cadastro")
    print("6 - Sair")
    return int(input("Escolha uma opcao: "))


def cadastrar_pessoa(lista_nomes, lista_idades, lista_emails):
    """Cadastra uma nova pessoa."""
    nome = input("Informe o nome: ")
    lista_nomes.append(nome)

    idade = int(input("Informe a idade: "))
    lista_idades.append(idade)

    email = input("Informe o email: ")
    lista_emails.append(email)

    if idade >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")


def exibir_pessoa(lista_nomes, lista_idades, lista_emails, pos):
    """Exibe os dados de uma pessoa."""
    print("Nome: " + lista_nomes[pos])
    print("Idade: " + str(lista_idades[pos]))
    print("E-mail: " + lista_emails[pos])

    if lista_idades[pos] >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")


def buscar_pessoa(lista_nomes, nome_procurado):
    """Busca uma pessoa pelo nome."""
    pos = 0

    while pos < len(lista_nomes):
        if lista_nomes[pos] == nome_procurado:
            return pos
        pos = pos + 1

    return -1


def consultar_pessoa(lista_nomes, lista_idades, lista_emails):
    """Consulta uma pessoa cadastrada."""
    procurado = input("Nome para consultar: ")
    pos = buscar_pessoa(lista_nomes, procurado)

    if pos == -1:
        print("Nao encontrado")
    else:
        exibir_pessoa(lista_nomes, lista_idades, lista_emails, pos)


def alterar_pessoa(lista_nomes, lista_idades, lista_emails):
    """Altera os dados de uma pessoa."""
    procurado = input("Nome para alterar: ")
    pos = buscar_pessoa(lista_nomes, procurado)

    if pos == -1:
        print("Nao encontrado")
    else:
        lista_nomes[pos] = input("Novo nome: ")
        lista_idades[pos] = int(input("Nova idade: "))
        lista_emails[pos] = input("Novo e-mail: ")
        print("Pessoa alterada!")
        exibir_pessoa(lista_nomes, lista_idades, lista_emails, pos)


def listar_pessoas(lista_nomes, lista_idades, lista_emails):
    """Lista todas as pessoas cadastradas."""
    if len(lista_nomes) == 0:
        print("Nenhuma pessoa cadastrada")

    pos = 0

    while pos < len(lista_nomes):
        exibir_pessoa(lista_nomes, lista_idades, lista_emails, pos)
        print("-------------------------")
        pos = pos + 1

    print("Total: " + str(len(lista_nomes)))


def analisar_faixa_etaria(idade):
    """Analisa a faixa etária de uma pessoa."""
    if idade < 12:
        print("Faixa etaria: crianca")
    elif idade < 18:
        print("Faixa etaria: adolescente")
    elif idade < 60:
        print("Faixa etaria: adulto")
    else:
        print("Faixa etaria: idoso")


def analisar_contato(idade, email):
    """Analisa a situação do contato."""
    if idade >= 18 and "@" in email:
        print("Contato: completo")
    elif idade >= 18:
        print("Contato: e-mail invalido")
    else:
        print("Contato: menor de idade")


def analisar_email(email):
    """Analisa o endereço de e-mail."""
    if "@" not in email:
        print("E-mail invalido")
    elif email.endswith("@gmail.com"):
        print("Provedor: Gmail")
    elif email.endswith("@outlook.com"):
        print("Provedor: Outlook")
    else:
        print("Provedor: outro")


def analisar_pessoa(lista_nomes, lista_idades, lista_emails):
    """Analisa os dados de uma pessoa."""
    procurado = input("Nome para analisar: ")
    pos = buscar_pessoa(lista_nomes, procurado)

    if pos == -1:
        print("Pessoa nao encontrada")
    else:
        idade = lista_idades[pos]
        email = lista_emails[pos]
        analisar_faixa_etaria(idade)
        analisar_email(email)
        analisar_contato(idade, email)


nomes = []
idades = []
emails = []

op = 0

while op != 6:
    op = exibir_menu()

    if op == 1:
        cadastrar_pessoa(nomes, idades, emails)
    elif op == 2:
        consultar_pessoa(nomes, idades, emails)
    elif op == 3:
        alterar_pessoa(nomes, idades, emails)
    elif op == 4:
        listar_pessoas(nomes, idades, emails)
    elif op == 5:
        analisar_pessoa(nomes, idades, emails)
    elif op == 6:
        print("Saindo...")
    else:
        print("Opcao invalida")

print("Fim do programa") 