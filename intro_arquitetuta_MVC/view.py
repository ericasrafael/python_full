# simulação de interface para interação com usuário

from mailbox import NotEmptyError
from controller import PersonC

while True:
    d = int(input(
        'Tecle 1 para efetuar um novo cadastro, 2 para visualuzar um cadastro, ou 3 para sair: '))
    if d == 3:
        break
    if d == 1:
        nome = input('nome: ')
        idade = int(input('idade: '))
        cpf = input('cpf: ')

        if PersonC.cadastrar(nome, idade, cpf):
            print('Caadstro efetuado com sucesso!')
        else:
            print('Digite valores válidos')
