from sqlite3 import dbapi2
import pymysql.cursors
from pathlib import Path
from time import sleep


# criando conexão com banco de dados criado (phpMyAdmin)

connection = pymysql.connect(
    host="localhost",  # hospedagem
    user="root",  # usuário
    password="",
    # referenciando banco de dados a serem executados os comandos SQL (USE DB)
    db="aula_bd_python_full",
    port=3306,
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)

def create_table(tabela):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE TABLE {tabela} (ID INT(4) AUTO_INCREMENT, PRIMARY KEY (ID))")
            print(f"Tabela TESTE criada com sucesso!")
    except Exception as e:
        error = str(repr(e))
        print(f"Error: {error}")

# create_table("TESTE")

# def func(tabela, **kwargs):
#     # print(f"CREATE TABLE {tabela} (NOME VARCHAR(100), IDADE INT(4), EMAIL VARCHAR(100), ENDEREÇO VARCHAR(150))")
#     for key, value in kwargs.items():
#         print(f"CREATE TABLE {tabela} ({key} {value})")

# func("TESTE", NOME="VARCHAR(100)",IDADE="INT(4)",EMAIL="VARCHAR(100),",ENDEREÇO="VARCHAR(150)")

def insert_new_columns():
    with open(Path(r'C:\Users\Erica Rafael\Desktop\python full\python + Banco de Dados\column_type_size.txt'), 'r') as arq:
        result = arq.readlines()
        tabela = result[0]
        print(tabela)
        result = list(map(lambda x: x.replace('\n', ''), result))
        for i in result[1:]:
                try:
                     with connection.cursor() as cursor:
                        cursor.execute(f"ALTER TABLE {tabela} ADD COLUMN {i}")
                        sleep(1)
                        print(f"COMANDO: [ ALTER TABLE TESTE ADD COLUMN {i} ] EFETUADO COM SUCESSO!")
                except Exception as e:
                    error = str(repr(e))
                    print(f"Error: {error}")

insert_new_columns()
            

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


def insert_into(table, insert_name):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO {table} VALUES ('{insert_name}')")
            print(
                f"Valor {insert_name} inserido com sucesso na tabela {table}!")
    except Exception as e:
        print(f"Error: {e}")

# for name in names:
#     insert_into("teste", name)

def select_data(table):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {table}")
            result = cursor.fetchall() # retornando todos os dados -> lista de dicionarios [{coluna:valor}]
                                       # cada dicionario é uma linha do banco de dados
            for i in result:
                print(i["nome"])
    except Exception as e:
        print(f"Error: {e}")

# select_data("teste")

def update_data(table, update_column, original_value, update_value):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"UPDATE {table} SET {update_column} = '{update_value}' WHERE {update_column} = '{original_value}'")                              
    except Exception as e:
        print(f"Error: {e}")

# update_data("teste", "nome", "Rafael", "Rafael Feitosa")

def delete_data(table, column, value):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"DELETE FROM {table} WHERE {column} = '{value}'")    
            print("Remoção efetuada com sucesso!")                          
    except Exception as e:
        print(f"Error: {e}")

# delete_data("teste", "nome", "Marcos Rafael")


