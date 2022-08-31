# Cadastro (Nome, Email, Senha)
# Login (Email, Senha) 
# OBS: segurança de sistema (criptografia de senha, força de senha, repetição de email)

from sqlalchemy import create_engine, Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USUARIO = "root"
SENHA = ""
HOST = "localhost"
BD = "BD_LOGIN"
PORT = 3306
CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BD}"
engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Pessoa(Base):
    __tablename__ = "pessoa"
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    email = Column(String(200))
    senha = Column(String(200))

Base.metadata.create_all(bind=engine)