from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Model import Pessoa


def Return_Session():
    USUARIO = "root"
    SENHA = ""
    HOST = "localhost"
    BD = "aula_bd_python_full"
    PORT = 3306

    CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BD}"

    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)

    return Session()

session = Return_Session()


# criando uma instância da classe Pessoa
a = Pessoa(nome="Joao", 
                usuario="joao", 
                senha="12345")

b = Pessoa(usuario="lucas", 
                senha="12345")

# CAMADAS: Python -> Session -> Engine ( Banco de Dados )

session.add_all([a,b]) # alterando na camada session
# session.rollback() # limpando a session, isso siginifica que as alterações não serão feitas no banco de dados
session.commit() # alterando no banco de dados