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
# c.cadastrar('Frios')
# c.remover('Higiene')
# c.alterar('Verduras','Carnes')
