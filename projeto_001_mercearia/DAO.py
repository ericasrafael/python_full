# Acesso aos Arquivos ( dados persistentes ) de armazenamento
# Armazena novos dados
# 002

from Models import *

# métodos de classe


class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):  # método para salvar novos dados em Categoria, recebe uma única string
        with open('categoria.txt', 'a') as arq:
            arq.writelines(categoria)  # cada linha é uma nova categoria
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()  # return list wich /n in each string
            print(cls.categoria)

        cls.categoria = list(map(lambda x: x.replace(
            '\n', ''), cls.categoria))  # removendo os \n
        print(cls.categoria)

        cat = list()
        for c in cls.categoria:
            # pois deve-se retornar a model (instância), cada i corresponde a uma string
            cat.append(Categoria(c))
        return cat


# DaoCategoria.salvar("Frutas")
# DaoCategoria.salvar("Legumes")
# DaoCategoria.salvar("Higiene")
# DaoCategoria.salvar("Verduras")
# DaoCategoria.ler()


class DaoVenda:
    @classmethod
    def salvar(cls, venda: Venda):  # recebe uma instância de Venda
        with open('venda.txt', 'a') as arq:
            arq.writelines(venda.item_vendido.nome + " || "
                           + venda.item_vendido.preco + " || "
                           + venda.item_vendido.categoria + " || "
                           + venda.vendedor + " || "
                           + venda.cliente + " || "
                           + str(venda.quantidade_vendida) + " || "
                           + venda.data)  # vendas recebe dado tipo Produto

            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('venda.txt', 'r') as arq:
            cls.venda = arq.readlines()
            print(cls.venda)
        cls.venda = list(map(lambda x: x.replace(
            '\n', ''), cls.venda))  # removendo os \n
        cls.venda = list(map(lambda x: x.split(' || '), cls.venda))
        print(cls.venda)
        vend = list()
        for i in cls.venda:
            vend.append(
                Venda(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))

        return vend

#p = Produtos("Banana","3","Frutas")
#v = Venda(p, "Erica", "Rafael" ,"8")
# DaoVenda.salvar(v)
# DaoVenda.ler()


class DaoEstoque:
    @classmethod
    def salvar(cls, produto: Produtos, quantidade):  # recebe uma instância de Produtos
        with open('estoque.txt', 'a') as arq:
            arq.writelines(produto.nome + " || "
                           + produto.preco + " || "
                           + produto.categoria + " || "
                           + str(quantidade))  # Estoque recebe dado tipo Produto
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()
        cls.estoque = list(map(lambda x: x.replace(
            '\n', ''), cls.estoque))  # removendo os \n
        cls.estoque = list(map(lambda x: x.split(' || '), cls.estoque))
        est = list()
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                est.append(Estoque(Produtos(i[0], i[1], i[2]), int(i[3])))

        return est


class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):  # recebe uma instância de Produtos
        with open('fornecedores.txt', 'a') as arq:
            arq.writelines(fornecedor.empresa + " || "
                           + fornecedor.cnpj + " || "
                           + fornecedor.contato + " || "
                           + fornecedor.categoria)  # Estoque recebe dado tipo Produto
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arq:
            cls.fornecedores = arq.readlines()
        cls.fornecedores = list(map(lambda x: x.replace(
            '\n', ''), cls.fornecedores))  # removendo os \n
        cls.fornecedores = list(
            map(lambda x: x.split(' || '), cls.fornecedores))
        forn = list()
        for i in cls.fornecedores:
            forn.append(Fornecedor(i[0], i[1], i[2], i[3]))

        return forn


class DaoPessoa:
    @classmethod
    def salvar(cls, pessoa: Pessoa):  # recebe uma instância de Produtos
        with open('clientes.txt', 'a') as arq:
            arq.writelines(pessoa.nome + " || "
                           + pessoa.contato + " || "
                           + pessoa.cpf + " || "
                           + pessoa.email + " || "
                           + pessoa.endereco)  # Estoque recebe dado tipo Produto
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('clientes.txt', 'r') as arq:
            cls.clientes = arq.readlines()
        cls.clientes = list(map(lambda x: x.replace(
            '\n', ''), cls.clientes))  # removendo os \n
        cls.clientes = list(map(lambda x: x.split(' || '), cls.clientes))
        cli = list()
        for i in cls.clientes:
            cli.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))

        return cli


class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):  # recebe uma instância de Produtos
        with open('funcionarios.txt', 'a') as arq:
            arq.writelines(funcionario.clt + " || "
                           + funcionario.nome + " || "
                           + funcionario.contato + " || "
                           + funcionario.cpf + " || "
                           + funcionario.email + " || "
                           + funcionario.endereco)  # Estoque recebe dado tipo Produto
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('funcionarios.txt', 'r') as arq:
            cls.funcionarios = arq.readlines()
        cls.funcionarios = list(map(lambda x: x.replace(
            '\n', ''), cls.funcionarios))  # removendo os \n
        cls.funcionarios = list(
            map(lambda x: x.split(' || '), cls.funcionarios))
        fun = list()
        for i in cls.funcionarios:
            fun.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5]))

        return fun
