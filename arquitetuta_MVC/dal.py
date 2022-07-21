# forma como os dados serão armazenados

from model import Person


class PersonD:
    @classmethod
    def salvar(cls, pessoa: Person):
        with open('Pessoas_Cadastradas.txt', 'a') as arq:
            arq.write(pessoa.nome + " " + str(pessoa.idade) + " " + pessoa.cpf)
