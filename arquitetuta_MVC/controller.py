from model import Person
from dal import PersonD

class PersonC:
    @classmethod
    def cadastrar(cls, nome,idade, cpf):
        if len(nome) > 0 and len(cpf) > 11:
            try:
                PersonD.salvar(Person(nome,idade,cpf))
                return True
            except:
                return False