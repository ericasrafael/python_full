from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USUARIO = "root"
SENHA = ""
HOST = "localhost"
BD = "aula_bd_python_full"
PORT = 3306
CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BD}"
# consexão com banco de dados
engine = create_engine(CONN, echo=True)
# criando sessão 
Session = sessionmaker(bind=engine)
session = Session()
# importando códigos nativos de banco de dados vindos do sqlAlchemy
Base = declarative_base()
# tabela no banco de dados passa ser uma classe na linguagem python


class Pessoa(Base):
    __tablename__ = "Pessoa"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    usuario = Column(String(20))
    senha = Column(String(10))


Base.metadata.create_all(engine)
