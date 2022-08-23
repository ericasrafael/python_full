# Interface gráfica: Contato com o Usuário
# 004

import Controller
import os.path

# cao no if apenas se arquivos não existirem


def criar_arquivos(*args):
    for i in args:
        if not os.path.exists(i):
            with open(i, "w") as arq:
                arq.write("")


criar_arquivos("categoria.txt", "estoque.txt",
               "clientes.txt", "fornecedores.txt",
               "funcionarios.txt", "venda.txt")

# só é verdadeiro se este arquivo .py for executado nele mesmo, ou seja,
# se a view for importada para outro arquivo .py o if retornaria False
if __name__ == "__main__":
    while True:
        local = int(input("Digite 1 para acessar [ Categorias ]\n"
                          "Digite 2 para acessar [ Estoque ] \n"
                          "Digite 3 para acessar [ Fornecedor ]\n"
                          "Digite 4 para acessar [ Clientes ]\n"
                          "Digite 5 para acessar [ Funcionario ]\n"
                          "Digite 6 para acessar [ Vendas ]\n"
                          "Digite 7 para acessar os produtos mais vendidos\n"
                          "Digite 8 para sair\n"))

        if local == 1:
            cat = Controller.ConCategoria()
            while True:
                decisao = int(input("Digite 1 para cadastrar uma categoria\n"
                                    "Digite 2 para remover uma categoria\n"
                                    "Digite 3 para alterar uma categoria\n"
                                    "Digite 4 para visualizar categorias cadastradas\n"
                                    "Digite 5 para sair\n"))

                if decisao == 1:
                    categoria = input(
                        "Digite a categoria que deseja cadastrar:\n")
                    cat.cadastrar(categoria)
                elif decisao == 2:
                    categoria = input(
                        "Digite a categoria que deseja remover:\n")
                    cat.remover(categoria)
                elif decisao == 3:
                    categoria_alterar = input(
                        "Digite a categoria que deseja alterar:\n")
                    categoria_nova = input(
                        "Digite a categoria para qual deseja alterar:\n")
                    cat.alterar(categoria_alterar, categoria_nova)
                elif decisao == 4:
                    cat.visualizar()
                else:
                    break  # voltando para menu principal

        elif local == 2:
            est = Controller.ConEstoque()
            while True:
                decisao = int(input("Digite 1 para cadastrar um produto\n"
                                    "Digite 2 para remover um produto\n"
                                    "Digite 3 para alterar um produto\n"
                                    "Digite 4 para visualizar o estoque\n"
                                    "Digite 5 para sair\n"))

                if decisao == 1:
                    nome = input("Digite o nome do produto:\n")
                    preco = input("Digite o preco do produto:\n")
                    categoria = input("Digite a categoria do produto:\n")
                    quantidade = input("Digite a quantidade do produto:\n")

                    est.cadastrar(nome, preco, categoria, quantidade)

                elif decisao == 2:
                    remover_produto = input(
                        "Digite o nome do produto que deseja remover:\n")
                    est.remover(remover_produto)

                elif decisao == 3:
                    produto_alterar = input(
                        "Digite o produto que deseja alterar:\n")
                    novo_produto = input(
                        "Digite o produto para qual deseja alterar:\n")
                    novo_preco = input("Digite o novo preco do produto:\n")
                    nova_categoria = input(
                        "Digite a nova cayegoria do produto:\n")
                    nova_quantidade = input(
                        "Digite a nova quantidade do produto")
                    est.alterar(produto_alterar, novo_produto,
                                novo_preco, nova_categoria, nova_quantidade)

                elif decisao == 4:
                    est.visualizar()
                else:
                    break  # voltando para menu principal

        elif local == 3:
            forn = Controller.ConFornecedor()
            while True:
                decisao = int(input("Digite 1 para cadastrar uma fornecedor\n"
                                    "Digite 2 para remover uma fornecedor\n"
                                    "Digite 3 para alterar uma fornecedor\n"
                                    "Digite 4 para visualizar fornecedores cadastrados\n"
                                    "Digite 5 para sair\n"))
                if decisao == 1:
                    empresa = input("Digite o nome do novo fornecedor:\n")
                    cnpj = input("Digite o CNPJ do novo fornecedor:\n")
                    contato = input("Digite o contato do novo fornecedor:\n")
                    categoria = input(
                        "Digite a categoria do novo fornecedor:\n")
                    forn.cadastrar(empresa, cnpj, contato, categoria)
                elif decisao == 2:
                    remover_fornecedor = input(
                        "Digite o nome do fornecedor que deseja remover:\n")
                    forn.remover(remover_fornecedor)
                elif decisao == 3:
                    alterar_fornecedor = input(
                        "Digite o fornecedor que deseja alterar:\n")
                    novo_fornecedor = input(
                        "Digite o produto para qual deseja alterar:\n")
                    novo_cnpj = input("Digite o novo preco do produto:\n")
                    novo_contato = input(
                        "Digite a nova cayegoria do produto:\n")
                    nova_categoria = input(
                        "Digite a nova quantidade do produto")
                    forn.alterar(alterar_fornecedor, novo_fornecedor,
                                 novo_cnpj, novo_contato, nova_categoria)
                elif decisao == 4:
                    forn.visualizar()
                else:
                    break

        elif local == 4:
            cli = Controller.ConCliente()
            while True:
                decisao = int(input("Digite 1 para cadastrar um cliente\n"
                                    "Digite 2 para remover uma cliente\n"
                                    "Digite 3 para alterar uma cliente\n"
                                    "Digite 4 para visualizar clientes cadastrados\n"
                                    "Digite 5 para sair\n"))
                if decisao == 1:
                    nome = input("Digite o nome do novo cliente:\n")
                    contato = input("Digite o contato do novo cliente:\n")
                    cpf = input("Digite o CPF do novo cliente:\n")
                    email = input("Digite o e-mail do novo cliente:\n")
                    endereco = input("Digite a endereco do novo cliente:\n")
                    cli.cadastrar(nome, contato, cpf, email, endereco)
                elif decisao == 2:
                    remover_cliente = input(
                        "Digite o nome do cliente que deseja remover:\n")
                    cli.remover(remover_cliente)
                elif decisao == 3:
                    alterar_cliente = input(
                        "Digite o nome do cliente que deseja alterar:\n")
                    novo_cliente = input(
                        "Digite o nome do cliente para qual deseja alterar:\n")
                    novo_contato = input("Digite o novo contato do cliente:\n")
                    novo_cpf = input("Digite a novo CPF do cliente:\n")
                    novo_email = input("Digite o novo e-mail do cliente")
                    nova_endereco = input("Digite o novo endereco do produto")
                    cli.alterar(alterar_cliente, novo_cliente,
                                novo_contato, novo_cpf, novo_email, nova_endereco)
                elif decisao == 4:
                    cli.visualizar()
                else:
                    break
        elif local == 5:
            func = Controller.ConFuncionario()
            while True:
                decisao = int(input("Digite 1 para cadastrar um funcionario\n"
                                    "Digite 2 para remover um funcionario\n"
                                    "Digite 3 para alterar um funcionario\n"
                                    "Digite 4 para visualizar funcionarios cadastrados\n"
                                    "Digite 5 para sair\n"))
                if decisao == 1:
                    clt = input("Digite a CLT do novo funcionario:\n")
                    nome = input("Digite o nome do novo funcionario:\n")
                    contato = input("Digite o contato do novo funcionario:\n")
                    cpf = input("Digite o CPF do novo funcionario:\n")
                    email = input("Digite o e-mail do novo funcionario:\n")
                    endereco = input("Digite a endereco do novo funcionario:\n")
                    func.cadastrar(clt,nome,contato,cpf,email, endereco)
                elif decisao == 2:
                    remover_funcionario = input(
                        "Digite o nome do funcionario que deseja remover:\n")
                    func.remover(remover_funcionario)
                elif decisao == 3:
                    alterar_funcionario = input(
                        "Digite o nome do funcionario que deseja alterar:\n")
                    novo_funcionario = input(
                        "Digite o nome do funcionario para qual deseja alterar:\n")
                    novo_clt = input("Digite a nova CLT do funcionario:\n")
                    novo_contato = input("Digite o novo contato do funcionario:\n")
                    novo_cpf = input("Digite a novo CPF do funcionario:\n")
                    novo_email = input("Digite o novo e-mail do funcionario:\n")
                    nova_endereco = input("Digite o novo endereco do funcionario: ")
                    func.alterar(alterar_funcionario, novo_funcionario, novo_clt, novo_contato, novo_cpf, novo_email, nova_endereco)
                elif decisao == 4:
                    func.visualizar()
                else:
                    break
        elif local == 6:
            vend = Controller.ConVenda()
            while True:
                decisao = int(input("Digite 1 para cadastrar uma nova venda\n"
                                    "Digite 2 para visualizar as vendas realizadas\n"
                                    "Digite 3 para sair\n"))
                if decisao == 1:
                    produto = input("Digite o produto vendido:\n")
                    vendedor = input("Digite o nome do vendedor:\n")
                    cliente = input("Digite o contato do cliente:\n")
                    quantidade = input("Digite a quantidade vendida:\n")
                    vend.cadastrar(produto, vendedor, cliente, quantidade)
                elif decisao == 2:
                    dataInicio = input("Digite a data de inicio no formato dia/mes/ano: \n")
                    dataTermino = input("Digite a data de termino no formato dia/mes/ano: \n")
                    vend.visualizar(dataInicio, dataTermino)
                else:
                    break
        elif local == 7:
            vend = Controller.ConVenda()
            vend.relatorioVendas()
        else:
            break
            
