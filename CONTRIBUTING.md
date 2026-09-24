# Guia de Contribuição

## Padrões de código

O projeto utiliza Python e segue boas práticas de organização e legibilidade de código.

* Utilizar nomes de funções e variáveis claros e descritivos.
* Utilizar indentação de 4 espaços.
* Utilizar docstrings nas funções.
* Evitar nomes de variáveis que possam causar conflito ou ambiguidade.
* Manter o código organizado e de fácil compreensão.

## Verificação com Pylint

Antes de realizar um commit, executar o Pylint para verificar possíveis problemas no código:

```bash
pylint cadastro.py
```

As mensagens encontradas devem ser analisadas e, quando aplicável, corrigidas antes do commit.

## Organização dos commits

Os commits devem ser pequenos e representar uma alteração específica.

Para alterações relacionadas à configuração ou documentação, utilizar o padrão:

```text
chore: descrição da alteração
```

Para alterações internas no código que não modificam o comportamento externo:

```text
refactor: descrição da alteração
```

As mensagens dos commits devem ser objetivas e descrever o que foi alterado.
