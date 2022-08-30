from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Model import Pessoa
from sqlalchemy import or_


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

# query = session.query(Pessoa).filter(Pessoa.id == 4).all()
# query[0].nome += " Rafael"
# query[0].senha = "675463946"
# query[0].usuario = "marcos123"

query = session.query(Pessoa).filter(Pessoa.id == 4).all()  # lista com todas as instâncias correspondentes
query = session.query(Pessoa).filter(Pessoa.id == 7).one()  # trás o próprio objeto, ou seja, a instância da classe Pessoa 

session.delete(query) # não exclui listas, apenas os objetos

session.commit()