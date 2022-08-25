from sqlite3 import dbapi2
import pymysql.cursors
from pathlib import Path

# criando conexão com banco de dados criado (phpMyAdmin)

connection = pymysql.connect(
    host="localhost",  # hospedagem
    user="root", # usuário
    password="",
    db="aula_bd_python_full", # referenciando banco de dados a serem executados os comandos SQL (USE DB)
    port=3306,
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)

with open(Path(r'C:\Users\Erica Rafael\Desktop\python full\python + Banco de Dados\names.txt'), 'r') as arq:
        names = arq.readlines() 
        names = list(map(lambda x: x.replace('\n', ''), names))  # removendo os \n
        print(names) 

def create_table(table):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE TABLE {table} ( nome varchar(100))")
            print(f"Tabela {table} criada com sucesso!")
    except Exception as e:
        print(f"Error: {e}")
        
# create_table("teste")

def drop_table(table):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"DROP TABLE {table}")
            print(f"Tabela {table} REMOVIDA com sucesso!")
    except Exception as e:
        print(f"Error: {e}")
        
# drop_table("teste")

# def insert_into(table):
#     insert_name = input("Digite o nome as ser inserido: ")
#     try:
#         with connection.cursor() as cursor:
#             cursor.execute(f"INSER INTO {table} VALUES({insert_name})")
#             print(f"Tabela {table} REMOVIDA com sucesso!")
#     except Exception as e:
#         print(f"Error: {e}")
        
# insert_into("teste")

def insert_into(table,insert_name):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO {table} VALUES ('{insert_name}')")
            print(f"Valor {insert_name} inserido com sucesso na tabela {table}!")
    except Exception as e:
        print(f"Error: {e}")
        
# insert_into("teste","Erica")
# insert_into("teste","Marcos")
# insert_into("teste","Rafael")
for name in names:
    insert_into("teste",name)