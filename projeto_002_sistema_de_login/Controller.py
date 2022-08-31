from Models import Pessoa
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import hashlib # criptografia dos dados

def return_session(USUARIO):
    SENHA = ""
    HOST = "localhost"
    BD = "BD_LOGIN"
    PORT = 3306
    CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BD}"
    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()
   

class ControllerCadastro():
    @classmethod
    def verificacao_de_dados(cls, nome, email, senha):
        if len(nome) > 100 or len(nome) < 3:
            return 2
        if len(email) > 200:
            return 3
        if len(senha) > 200 or len(senha) < 6:
            return 4
        return 1

    @classmethod
    def cadastrar(cls, nome, email, senha):
        session = return_session("root")
        usuario = session.query(Pessoa).filter(Pessoa.email == email).all()  # pega todos os emails que forem iguais ao que está tentando ser cadastrado no momento
        if len(usuario) > 0:
            return 5
        dados_verificados = cls.verificacao_de_dados(nome, email, senha)
        if dados_verificados != 1:
            return dados_verificados
        try:
            senha = hashlib.sha256(senha.encode()).hexdigest()
            p = Pessoa(nome=nome, email=email, senha=senha)   
            session.add(p)
            session.commit()
            return 1
        except:
            return 6

# print(ControllerCadastro.cadastrar("Erica Rafael", "ericasrafael@gmail.com", "erica12345"))

class ControllerLogin():
    @classmethod
    def login(cls, email, senha):
        session = return_session("root")
        senha = hashlib.sha256(senha.encode()).hexdigest() 
        logado = session.query(Pessoa).filter(Pessoa.email == email).filter(Pessoa.senha == senha).all()

        if len(logado) == 1:
            return {'logado':True, "id": logado[0].id }
        else:
            return False

# print(ControllerLogin.login("ericasrafael@gmail.com", "erica12345"))