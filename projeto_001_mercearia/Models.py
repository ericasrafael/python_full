# Classes: Onde serão armazenado as informações relevantes ao cliente
# Definição e Estruturação de Dados, características dos dados

from datetime import datetime


class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria

class Produtos:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

class Estoque:
    def __init__(self, produto: Produtos, quantidade):  # variável é do tipo Produtos
        self.produto = produto
        self.quantidade = quantidade

class Venda:
    # por padrão, pega data do sistema operacional
    def __init__(self, item_vendido: Produtos, vendedor, cliente, quantidade_vendida, data=datetime.now()):
        self.item_vendido = item_vendido
        self.vendedor = vendedor
        self.cliente = cliente
        self.quantidade_vendida = quantidade_vendida
        self.data = data

class Fornecedor:
    def __init__(self, empresa, cnpj, contato, categoria):
        self.empresa = empresa
        self.cnpj = cnpj
        self.contato = contato
        self.categoria = categoria

class Pessoa:
    def __init__(self, nome, contato, cpf, email, endereco):
        self.nome = nome
        self.contato = contato
        self.endereco = endereco
        self.cpf = cpf
        self.email = email
        self.endereco = endereco

class Funcionario(Pessoa):
    def __init__(self, clt, nome, contato, cpf, email, endereco):
        self.clt = clt
        super(Funcionario).__init__(nome, contato, cpf, email, endereco)