# Lógica da Estruturação dos Dados: Segurança, verificações, novos dados, remoção de dados, lógica do sistema
# 003

from Models import *
from DAO import *
from datetime import datetime

# métodos de instância


class ConCategoria:
    def cadastrar(self, novaCategoria):  # cadastrar categoria
        existe = False
        x = DaoCategoria.ler()  # return list

        for i in x:
            if i.categoria == novaCategoria:
                existe = True

        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print('Categoria Cadastrada com Sucesso!')
        else:
            print('A Categoria  que deseja cadastrar já Existe!')

    def remover(self, categoriaRemove):  # remover categoria
        x = DaoCategoria.ler()  # return list

        # retorna para cat apenas categoria que seja igual a repassada como parâmetro de ConCategoria().remover()
        cat = list(filter(lambda x: x.categoria == categoriaRemove, x))

        if len(cat) <= 0:
            print('A categoria especificada não existe!')

        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemove:  # removendo da memória RAM
                    del x[i]
                    break
            print('Categoria(s) removida(s) com sucesso!')
        # TODO: colocar 'Sem Categoria' em estoque.txt
            with open('categoria.txt', 'w') as arq:
                for i in x:
                    # reescrevendo no arquivo as categorias restantes em x
                    arq.writelines(i.categoria)
                    arq.writelines('\n')

        estoque = DaoEstoque.ler()
        # alterar dados = map()
        estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, "Produto Sem Categoria"), x.quantidade)
                           if(x.produto.categoria == categoriaRemove) else(x), estoque))  # memória RAM

        with open("estoque.txt", "w") as arq:
            for i in estoque:
                arq.writelines(i.produto.nome + " || "
                               + i.produto.preco + " || "
                               + i.produto.categoria + " || "
                               + str(i.quantidade))
                arq.writelines('\n')

    def alterar(self, original, alterada):  # alterando categoria
        x = DaoCategoria.ler()  # return list of categories

        # a categoria que deseja alterar deve existir em DeoCategoria
        cat = list(filter(lambda x: x.categoria == original, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == alterada, x))
            if len(cat1) == 0:
                # alterando arquivo na memória RAM, substituindo o parâmetro 'original' por 'alterada'
                x = list(map(lambda x: Categoria(alterada) if(
                    x.categoria == original) else(x), x))
                print('Categoria alterada com sucesso!')
                
                estoque = DaoEstoque.ler()
                # alterar dados = map()
                estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, alterada), x.quantidade)
                           if(x.produto.categoria == original) else(x), estoque))  # memória RAM

                with open("estoque.txt", "w") as arq:
                    for i in estoque:
                        arq.writelines(i.produto.nome + " || "
                                    + i.produto.preco + " || "
                                    + i.produto.categoria + " || "
                                    + str(i.quantidade))
                        arq.writelines('\n')
            else:
                print("A categoria para qual deseja alterar já existe!")
        else:
            print('A categoria que deseja alterar não existe!')
        # TODO: alterar em estoque.txt relativamente
        with open('categoria.txt', 'w') as arq:
            # reescrevendo no arquivo as alterações
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

    def visualizar(self):  # printando as categorias existentes
        categorias = DaoCategoria.ler()
        if len(categorias) == 0:
            print('Nenhuma categoria cadastrada!')
        else:
            for i in categorias:
                print(f'Categoria: {i.categoria}')


c = ConCategoria()
# c.cadastrar('Frios')
# c.cadastrar('Verduras')
# c.cadastrar('Frutas')
# c.cadastrar('Laticinios')
# c.cadastrar('Legumes')
# c.cadastrar('Higiene')
# c.remover('Frios')
c.alterar('Laticinios','Verduras')
# c.visualizar()


class ConEstoque:
    def cadastrar(self, nome, preco, categoria, quantidade):
        e = DaoEstoque.ler()  # return list
        c = DaoCategoria.ler()  # return list

        # veriifcando se categoria repassada como parâmetro existe cadastrada em Categoria.txt

        h = list(filter(lambda c: c.categoria == categoria, c))
        est = list(filter(lambda e: e.produto.nome == nome, e))

        # para cadastrar, o produto não deve já estar cadastrado em Estoque.txt, mas deve conter sua categoria em Categoria.txt
        if len(h) > 0:
            if len(est) == 0:
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print('Produto cadastrado com sucesso!')
            else:
                print('Este produto já existe no Estoque')
        else:
            print('Categoria inexistente!')

    def remover(self, nome):
        e = DaoEstoque.ler()
        est = list(filter(lambda e: e.produto.nome == nome, e))

        if len(est) > 0:
            # iterando por cada produto cadstrado em estoque
            for i in range(len(e)):
                if e[i].produto.nome == nome:
                    del e[i]
                    break
            print('Produto removido do Estoque com sucesso!')
        else:
            print('Este produto não existe no Estoque!')

        with open('Estoque.txt', 'w') as arq:
            for i in e:
                arq.writelines(i.produto.nome + " || "
                               + i.produto.preco + " || "
                               + i.produto.categoria + " || "
                               + str(i.quantidade))  # Estoque recebe dado tipo Produto
                arq.writelines('\n')

    def alterar(self, nomeOriginal, nomeNovo, precoNovo, categoriaNova, quantidadeNova):
        e = DaoEstoque.ler()
        c = DaoCategoria.ler()

        h = list(filter(lambda c: c.categoria == categoriaNova, c))

        if len(h) > 0:
            est = list(filter(lambda e: e.produto.nome == nomeOriginal, e))
            if len(est) > 0:
                est = list(filter(lambda e: e.produto.nome == nomeNovo, e))
                if len(est) == 0:
                    # alterando e, que é a lista de produtos cadastrados retornados de DaoEstoque.ler()
                    e = list(map(lambda e: Estoque(Produtos(nomeNovo, precoNovo, categoriaNova), quantidadeNova) if(
                        e.produto.nome == nomeOriginal) else(e), e))
                    print('Produto alterado no Estoque!')
                else:
                    print('O produto para qual deseja alterar já está cadastrado!')
            else:
                print('O produto o qual deseja alterar não está cadastrado!')

            with open('estoque.txt', 'w') as arq:
                for i in e:
                    arq.writelines(i.produto.nome + " || "
                                   + i.produto.preco + " || "
                                   + i.produto.categoria + " || "
                                   + str(i.quantidade))  # Estoque recebe dado tipo Produto
                    arq.writelines('\n')
        else:
            print('A categoria repassada não está cadastrada!')

    def visualizar(self):
        estoque = DaoEstoque.ler()
        if len(estoque) == 0:
            print('Estoque vazio!')
        else:
            print('===========Produtos===========')
            for i in estoque:
                print(f'Nome: {i.produto.nome}\n'
                      f'Preco: {i.produto.preco}\n'
                      f'Categoria: {i.produto.categoria}\n'
                      f'Quantidade: {i.quantidade}\n')
                print('==============================')


# e = ConEstoque()
# e.cadastrar('Uva','6','Frutas',100)
# e.cadastrar('Banana','8','Frutas',40)
# e.cadastrar('Laranja','3','Frutas',70)
# e.cadastrar('Tangerina','4','Frutas',50)
# e.remover('Uva')
# e.alterar('Uva','Tangerina','4','Frutas',50)
# e.visualizar()

class ConVenda:
    def cadastrar(self, nomeProduto, vendedor, cliente, quantidadeVendida):
        e = DaoEstoque.ler()  # precisa existir produto no estoque
        temp = list()
        existe = False
        # quantidade vendida precisa ser inferior ou igual a quantidade em estoque
        quantidade = False
        for i in e:
            if existe == False:
                if i.produto.nome == nomeProduto:
                    existe = True  # contém o produto em estoque
                    if i.quantidade >= quantidadeVendida:
                        quantidade = True

                        # atualizando a quantidade do produto em estoque após a venda
                        i.quantidade = int(i.quantidade) - \
                            int(quantidadeVendida)

                        # cadastrando a venda, com o produto vendido ( passou por todos os if's )
                        vendido = Venda(Produtos(i.produto.nome, i.produto.preco,
                                        i.produto.categoria), vendedor, cliente, quantidadeVendida)

                        # calculando o valor da venda
                        valorDaCompra = int(
                            quantidadeVendida) * float(i.produto.preco)

                        DaoVenda.salvar(vendido)

            # contém todos os valores de estoque, somente com quantidade do produto vendido atualizada
            temp.append(Estoque(Produtos(i.produto.nome,
                        i.produto.preco, i.produto.categoria), i.quantidade))

        arq = open('estoque.txt', 'w')
        arq.write('')  # limpando arquivo

        for i in temp:
            with open('estoque.txt', 'a') as arq:
                arq.writelines(i.produto.nome + ' || ' + i.produto.preco +
                               ' || ' + i.produto.categoria + ' || ' + str(i.quantidade))
                arq.writelines('\n')

        # colocando na View
        if existe == False:
            print('Este produto nao esta disponivel em Estoque!')
            return None
        elif not quantidade:
            print(
                'Nao ha quantidade suficiente referente a este produto no Estoque para efetuar a venda!')
            return None
        else:
            print('Venda realizada com sucesso!')
            return valorDaCompra

    # Relatorio de produtos mais vendidos
    def relatorioVendas(self):
        vendas = DaoVenda.ler()
        produtos = list()

        # percorrendo cada venda cadastrada
        for i in vendas:
            nome = i.item_vendido.nome
            quantidade = i.quantidade_vendida
            # verificando se um produto foi vendido mais de uma vez, para poder somar as quantidades dentro de produtos list
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))

            if len(tamanho) > 0:
                produtos = list(map(lambda x: {
                                'produto': nome, 'quantidade': int(x['quantidade']) + int(quantidade)} if(x['produto'] == nome) else(x), produtos))
            else:
                produtos.append(
                    {'produto': nome, 'quantidade': int(quantidade)})

        # ordenando pela quantidade de itens vendidos daquele produto
        ordenado = sorted(
            produtos, key=lambda x: x['quantidade'], reverse=True)

        print('Produtos mais vendidos:')
        a = 1
        for i in ordenado:
            print(f"============ Produto {a} ============")
            print(f" Produto: {i['produto']}\n"
                  f" Quantidade: {i['quantidade']}\n")
            a += 1

    def visualizar(self, inicio, termino):
        vendas = DaoVenda.ler()
        dataIninio = datetime.strptime(inicio, '%d/%m/%Y')
        dataFim = datetime.strptime(termino, '%d/%m/%Y')

        vendasSelecionadas = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= dataIninio
                                         and datetime.strptime(x.data, '%d/%m/%Y') <= dataFim, vendas))

        total = 0
        for i in vendasSelecionadas:
            print('=======================================')
            print(f"Nome: {i.item_vendido.nome}\n"
                  f"Categoria: {i.item_vendido.categoria}\n"
                  f"Data da Venda: {i.data}\n"
                  f"Quantidade Vendida: {i.quantidade_vendida}\n"
                  f"Cliente: {i.cliente}\n"
                  f"Vendedor: {i.vendedor}")

            total += float(i.item_vendido.preco) * int(i.quantidade_vendida)

        print(f"Total vendido foi de: R${total}")


# v = ConVenda()
# v.cadastrar('Laranja','Erica','Rafael',10)
# v.cadastrar('Tangerina','Erica','Rafael',10)
# v.cadastrar('Tangerina','Natalia','Joao',10)
# v.cadastrar('Banana','Erica','Rafael',10)
# v.cadastrar('Uva','Natalia','Rafael',10)
# v.relatorioVendas()
# v.visualizar('20/07/2022','25/07/2022')

class ConFornecedor:
    def cadastrar(self, empresa, cnpj, contato, categoria):
        f = DaoFornecedor.ler()
        # atributos que não podem se repetir entre os cadastros dos fornecedores
        listaCnpj = list(filter(lambda x: x.cnpj == cnpj, f))
        listaContato = list(filter(lambda x: x.contato == contato, f))

        if len(listaCnpj) > 0:
            print('Este CNPJ já está cadastrado!')
        elif len(listaContato) > 0:
            print('Este telefone já está cadastrado!')
        else:
            if len(cnpj) == 14 and (len(contato) <= 11 and len(contato) >= 10):
                DaoFornecedor.salvar(Fornecedor(
                    empresa, cnpj, contato, categoria))
                print('Fornecedor cadastrado com sucesso!')
            else:
                print('Telefone e/ou CNPJ inválido(s)!')

    def alterar(self, empresaOriginal, empresaAlterado, cnpjAlterado, contatoAlterado, categoriaAlterada):
        f = DaoFornecedor.ler()
        # atributos que não podem se repetir em Fornecedores()
        empresaCadastradas = list(
            filter(lambda x: x.empresa == empresaOriginal, f))

        # se o nome que deseja alterar estiver cadastrado
        if len(empresaCadastradas) > 0:
            # verificar se cnpj que deseja alterar já está cadstrado
            cnpjCadastrados = list(filter(lambda x: x.cnpj == cnpjAlterado, f))
            if len(cnpjCadastrados) == 0:
                # modificando os dados na memória RAM
                x = list(map(lambda x: Fornecedor(empresaAlterado, cnpjAlterado, contatoAlterado, categoriaAlterada
                                                  if(x.empresa == empresaOriginal) else(x), f)))
            else:
                print('O CNPJ para o qual deseja alterar já está cadastrado!')
        else:
            print('O fornecedor que deseja alterar não está cadastrado!')

        # modificando os dados no disco rígido
        with open('fornecedores.txt', 'w') as arq:
            for i in x:
                # Estoque recebe dado tipo Produto
                arq.writelines(i.empresa + " || " + i.cnpj +
                               " || " + i.contato + " || " + i.categoria)
                arq.writelines('\n')
            print('Fornecedor alterado com sucesso!')

    def remover(self, empresaRemove):  # remover categoria
        f = DaoFornecedor.ler()  # return list

        emp = list(filter(lambda x: x.empresa == empresaRemove, f))

        if len(emp) > 0:
            for i in range(len(f)):
                if f[i].empresa == empresaRemove:  # removendo da memória RAM
                    del f[i]
                    break
                else:
                    print('Este fornecedor não está cadastrado!')
                    return None
            # modificando os dados no disco rígido
            with open('fornecedores.txt', 'w') as arq:
                # Estoque recebe dado tipo Produto
                arq.writelines(i.empresa + " || " + i.cnpj +
                               " || " + i.contato + " || " + i.categoria)
                arq.writelines('\n')
            print('Fornecedor removido com sucesso!')

    def visualizar(self):  # printando as categorias existentes
        fornecedores = DaoFornecedor.ler()
        if len(fornecedores) == 0:
            print('Não há fornecedores cadastrados!')
        else:
            for i in fornecedores:
                print('========= FORNECEDORES =========')
                print(f'Categoria fornecida: {i.categoria}\n'
                      f'Nome do fornecedor: {i.empresa}\n'
                      f'Contato: {i.contato}\n'
                      f'CNPJ: {i.cnpj}\n')


class ConCliente:
    def cadastrar(self, nome, contato, cpf, email, endereco):
        c = DaoPessoa.ler()
        # atributos que não podem se repetir entre os cadastros dos fornecedores
        cpfCadastrados = list(filter(lambda x: x.cpf == cpf, c))

        if len(cpfCadastrados) > 0:
            print('Este CPF já está cadastrado!')
        else:
            if len(cpf) == 11 and (len(contato) <= 11 and len(contato) >= 10):
                DaoPessoa.salvar(Pessoa(nome, contato, cpf, email, endereco))
                print('Cliente cadastrado com sucesso!')
            else:
                print('Telefone e/ou CPF inválido(s)!')

    def alterar(self, nomeOriginal, nomeAlterado, cpfAlterado, contatoAlterado, emailAlterado, enderecoAlterado):
        c = DaoPessoa.ler()
        # atributos que não podem se repetir em Fornecedores()
        clientesCadastrados = list(filter(lambda x: x.nome == nomeOriginal, c))
        # se o nome que deseja alterar estiver cadastrado
        if len(clientesCadastrados) > 0:
            # verificar se cpf que deseja alterar já está cadstrado
            cpfCadastrados = list(filter(lambda x: x.cpf == cpfAlterado, c))
            if len(cpfCadastrados) == 0:
                # modificando os dados na memória RAM
                x = list(map(lambda x: Pessoa(nomeAlterado, contatoAlterado, cpfAlterado, emailAlterado, enderecoAlterado)
                             if(x.nome == nomeOriginal) else(x), c))
            else:
                print('O CPF para o qual deseja alterar já está cadastrado!')
        else:
            print('O cliente que deseja alterar não está cadastrado!')

        # modificando os dados no disco rígido
        with open('clientes.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + " || " + i.contato + " || " + i.cpf + " || " +
                               i.email + " || " + i.endereco)
                arq.writelines('\n')
            print('Cliente alterado com sucesso!')

    def remover(self, nome):  # remover cliente
        c = DaoPessoa.ler()  # return list

        # retorna para pes apenas cliente que seja igual a repassada como parâmetro de ConCliente().remover()
        pes = list(filter(lambda x: x.nome == nome, c))

        if len(pes) > 0:
            for i in range(len(c)):
                if c[i].nome == nome:  # removendo da memória RAM
                    del c[i]
                    break
                else:
                    print('Este cliente não está cadastrado!')
                    return None
            # modificando os dados no disco rígido
            with open('clientes.txt', 'w') as arq:
                for i in c:
                    arq.writelines(i.nome + " || " + i.contato + " || " + i.cpf + " || " +
                                   i.email + " || " + i.endereco)
                    arq.writelines('\n')
                print('Cliente removido com sucesso!')


class ConFuncionario:
    def cadastrar(self, clt, nome, contato, cpf, email, endereco):
        f = DaoFuncionario.ler()
        # atributos que não podem se repetir entre os cadastros dos fornecedores
        lista_cpf = list(filter(lambda x: x.cpf == cpf, f))
        lista_clt = list(filter(lambda x: x.clt == clt, f))

        if len(lista_cpf) > 0:
            print('Este CPF ja esta cadastrado!')
        elif len(lista_clt) > 0:
            print('Esta CLT ja esta cadastrada!')
        else:
            if len(cpf) == 11 and (len(contato) <= 11 and len(contato) >= 10):
                DaoFuncionario.salvar(Funcionario(
                    clt, nome, contato, cpf, email, endereco))
                print('Funcionario cadastrado com sucesso!')
            else:
                print('Telefone e/ou CPF inválido(s)!')

    def alterar(self, nomeOriginal, nomeAlterado, cltAlterado, contatoAlterado, cpfAlterado, emailAlterado, enderecoAlterado):
        f = DaoFuncionario.ler()
        # atributos que não podem se repetir em Fornecedores()
        func_cadastrado = list(
            filter(lambda x: x.empresa == nomeOriginal, f))

        # se o nome que deseja alterar estiver cadastrado
        if len(func_cadastrado) > 0:
            # verificar se cnpj que deseja alterar já está cadstrado
            cltCadastrados = list(filter(lambda x: x.clt == cltAlterado, f))
            if len(cltCadastrados) == 0:
                # modificando os dados na memória RAM
                x = list(map(lambda x: Funcionario(cltAlterado, nomeAlterado, contatoAlterado, cpfAlterado, emailAlterado, enderecoAlterado
                                                   if(x.nome == nomeOriginal) else(x), f)))
            else:
                print('A CLT para o qual deseja alterar já está cadastrada!')
        else:
            print('O funcionário que deseja alterar não está cadastrado!')

        # modificando os dados no disco rígido
        with open('funcionarios.txt', 'w') as arq:
            for i in x:
                # Estoque recebe dado tipo Produto
                arq.writelines(i.empresa + " || " + i.cnpj +
                               " || " + i.contato + " || " + i.categoria)
                arq.writelines('\n')
            print('Funcionario alterado com sucesso!')

    def remover(self, nome):  # remover cliente
        c = DaoFuncionario.ler()  # return list

        # retorna para pes apenas cliente que seja igual a repassada como parâmetro de ConCliente().remover()
        pes = list(filter(lambda x: x.nome == nome, c))

        if len(pes) > 0:
            for i in range(len(c)):
                if c[i].nome == nome:  # removendo da memória RAM
                    del c[i]
                    break
                else:
                    print('Este funcionario não está cadastrado!')
                    return None
            # modificando os dados no disco rígido
            with open('funcionarios.txt', 'w') as arq:
                for i in c:
                    arq.writelines(i.nome + " || " + i.contato + " || " + i.cpf + " || " +
                                   i.email + " || " + i.endereco)
                    arq.writelines('\n')
                print('Funcionario removido com sucesso!')

    def visualizar():
        funcionario = Funcionario.ler()
        if len(funcionario) == 0:
            print('Lista de funcionarios esta vazia!')
        for i in funcionario:
            print('====== Funcionario ======')
            print(f'Nome: {i.nome}\n'
                  f'CLT: {i.clt}\n'
                  f'Telefone: {i.contato}\n'
                  f'CPF: {i.cpf}\n'
                  f'E-mail: {i.email}\n'
                  f'Endereço: {i.endereco}')
