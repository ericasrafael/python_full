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

#c = ConCategoria()
#c.cadastrar('Frios')
#c.cadastrar('Verduras')
#c.cadastrar('Frutas')
#c.cadastrar('Laticinios')
#c.cadastrar('Legumes')
#c.cadastrar('Higiene')
#c.remover('Higiene')
#c.alterar('Verduras','Carnes')
#c.visualizar()

class ConEstoque:
    def cadastrar(self, nome, preco, categoria, quantidade):
        e = DaoEstoque.ler() # return list
        c = DaoCategoria.ler() # return list
        
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
        
        if len(h) > 0 :
            est = list(filter(lambda e: e.produto.nome == nomeOriginal, e))
            if len(est) > 0:
                est = list(filter(lambda e: e.produto.nome == nomeNovo, e))
                if len(est) == 0:
                    # alterando e, que é a lista de produtos cadastrados retornados de DaoEstoque.ler()
                    e = list(map(lambda e: Estoque(Produtos(nomeNovo, precoNovo, categoriaNova),quantidadeNova) if(e.produto.nome == nomeOriginal) else(e), e))
                    print('Produto alterado no Estoque!')
                else:
                    print('O produto para qual deseja alterar já está cadastrado!')          
            else:
                print('O produto o qual deseja alterar não está cadastrado!')
                
            with open('estoque.txt','w') as arq:
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
                    
    
               
#e = ConEstoque()
#e.cadastrar('Uva','6','Frutas',50)
#e.cadastrar('Banana','8','Frutas',40)
#e.cadastrar('Laranja','3','Frutas',70)
#e.remover('Uva')
#e.alterar('Uva','Tangerina','4','Frutas',50)
#e.visualizar()

class ConVenda:
    def cadastrar(self, nomeProduto, vendedor, cliente, quantidadeVendida):
        e = DaoEstoque.ler()  # precisa existir produto no estoque
        temp = list()
        existe = False
        quantidade = False  # quantidade vendida precisa ser inferior ou igual a quantidade em estoque
        for i in e:
            if existe == False:
                if i.produto.nome == nomeProduto:
                    existe = True  # contém o produto em estoque
                    if i.quantidade >= quantidadeVendida:
                        quantidade = True
                        
                        # atualizando a quantidade do produto em estoque após a venda
                        i.quantidade = int(i.quantidade) - int(quantidadeVendida)
                        
                        # cadastrando a venda, com o produto vendido ( passou por todos os if's )
                        vendido = Venda(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, cliente, quantidadeVendida)
                        
                        # calculando o valor da venda
                        valorDaCompra = int(quantidadeVendida) * float(i.produto.preco)
                        
                        DaoVenda.salvar(vendido)
                        
            temp.append([Produtos(i.produto.nome, i.produto.preco, i.produto.categoria),i.quantidade])
            
            arq = open('estoque.txt','w')
            arq.write('') # limpando arquivo
            
            for i in temp:
                with open('estoque.txt','a') as arq:
                    arq.writelines(i[0].nome + ' || ' + i[0].preco + ' || ' + i[0].categoria + ' || ' + str(i[1]))
                    arq.writelines('\n')
            
        # colocando na View
        if existe == False:
            print('Este produto nao esta disponivel em Estoque!')
            return None
        elif not quantidade:
            print('Nao ha quantidade suficiente referente a este produto no Estoque para efetuar a venda!')
            return None
        else:
            print('Venda realizada com sucesso!')
            return valorDaCompra
        
v = ConVenda()
v.cadastrar('Laranja','Erica','Rafael',10)     