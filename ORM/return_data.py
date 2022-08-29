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

consulta = session.query(Pessoa).all() # retorna uma lista onde cada posição é uma instância

for i in consulta:
    print(i.usuario)

consulta = session.query(Pessoa).filter(Pessoa.nome == 'Erica')
for i in consulta:
    print(i.usuario)

consulta = session.query(Pessoa).filter_by(nome = 'Erica', usuario = "ericasrafael")
for i in consulta:
    print(i.id)

consulta = session.query(Pessoa).filter(or_(Pessoa.nome == "Erica", Pessoa.usuario == "lucas")).all()
for i in consulta:
    print(i.id)