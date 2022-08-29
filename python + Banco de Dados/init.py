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


table = "CADASTRO"


def create_table(tabela):
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {tabela} (ID INT(4) AUTO_INCREMENT, PRIMARY KEY (ID))")
            print(f"Tabela {tabela} criada com sucesso!")
    except Exception as e:
        error = str(repr(e))
        print(f"Error: {error}")

# create_table(table)


def insert_new_columns():
    with open(Path(r'C:\Users\Erica Rafael\Desktop\python full\python + Banco de Dados\arquivos\column_type_size.txt'), 'r') as arq:
        colunas = arq.readlines()

    tabela = colunas[0].replace("TABELA: ", "")
    colunas = list(map(lambda x: x.replace('\n', ''), colunas[1:]))

    with open(Path(r'C:\Users\Erica Rafael\Desktop\python full\python + Banco de Dados\arquivos\new_columns.txt'), 'r') as arq:
        colunas_novas = arq.readlines()

    colunas_novas = list(map(lambda x: x.replace('\n', ''), colunas_novas))

    set_colunas = set(colunas)
    set_colunas_novas = set(colunas_novas)
    diff = set_colunas.difference(set_colunas_novas)

    if len(diff) > 0:
        with open(Path(r'C:\Users\Erica Rafael\Desktop\python full\python + Banco de Dados\arquivos\new_columns.txt'), 'w') as arq:
            padrao = list()
            for coluna in colunas:
                arq.writelines(coluna + "\n")
                coluna = coluna.split(" ")[0]
                padrao.append(coluna)
            # pega todos os itens em um iterável e os une em uma string
            padrao = ', '.join(padrao)
        with open(Path(r'C:\Users\Erica Rafael\Desktop\python full\python + Banco de Dados\arquivos\insert_values.txt'), 'r') as arq:
            lines = arq.readlines()
        with open(Path(r'C:\Users\Erica Rafael\Desktop\python full\python + Banco de Dados\arquivos\insert_values.txt'), 'w') as arq:
            for index, line in enumerate(lines):
                if index == 1:
                    arq.writelines(padrao+"\n")
                else:
                    arq.writelines(line)
        try:
            with connection.cursor() as cursor:
                for i in diff:
                    cursor.execute(f"ALTER TABLE {tabela} ADD COLUMN {i}")
                    sleep(2)
                    print(
                        f"Comando: [ ALTER TABLE {tabela} ADD COLUMN {i} ] efetuado com sucesso!")
        except Exception as e:
            error = str(repr(e))
            print(f"Error: {error}")

# insert_new_columns()


def drop_table(tabela):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"DROP TABLE {tabela}")
            print(f"Tabela {tabela} removida com sucesso!")
    except Exception as e:
        print(f"Error: {e}")

# drop_table(table)


def insert_into_values():
    with open(Path(r'C:\Users\Erica Rafael\Desktop\python full\python + Banco de Dados\arquivos\column_type_size.txt'), 'r') as arq:
        lines = arq.readlines()
    tabela = lines[0].replace("TABELA: ", "")

    with open(Path(r'C:\Users\Erica Rafael\Desktop\python full\python + Banco de Dados\arquivos\insert_values.txt'), 'r') as arq:
        lines = arq.readlines()
    colunas = lines[1]
    valores = list(map(lambda x: x.replace("\n", ""), lines[2:]))
    for valor in valores:
        valor = valor.split(", ")
        valor = str(valor)
        valor = valor.replace("[", "").replace("]", "")
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    f"INSERT INTO {tabela}({colunas}) VALUES ({valor})")
                sleep(1)
                print(f"Valor inserido com sucesso na tabela {tabela}!")
        except Exception as e:
            print(f"Error: {e}")

# insert_into_values()


def select_data(tabela):
    try:
        data = list()
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {tabela}")
            # retornando todos os dados -> lista de dicionarios [{coluna:valor}]
            results = cursor.fetchall()
            # cada dicionario é uma linha do banco de dados
            for result in results:
                data.append(result)
    except Exception as e:
        print(f"Error: {e}")
    print(data)  # lista de dicionários

# select_data(table)


def update_value():

    with open(Path(r'C:\Users\Erica Rafael\Desktop\python full\python + Banco de Dados\arquivos\update_value.txt'), 'r') as arq:
        lines = arq.readlines()

    lines = list(map(lambda x: x.replace("\n", ""), lines))
    tabela = lines[0].replace("TABELA: ", "")
    coluna_atualizar = lines[1].replace("COLUNA A SER ATUALIZADA: ", "")
    novo_valor = lines[2].replace("NOVO VALOR DA COLUNA: ", "")
    where = lines[3].replace("COLUNA BASE: ", "")
    valor_where = lines[4].replace("VALOR DA COLUNA BASE: ", "")

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                f"UPDATE {tabela} SET {coluna_atualizar} = '{novo_valor}' WHERE {where} = '{valor_where}'")
            print(
                f"UPDATE {tabela} SET {coluna_atualizar} = '{novo_valor}' WHERE {where} = '{valor_where}'")
    except Exception as e:
        print(f"Error: {e}")

# update_value()


def delete_data():
    with open(Path(r'C:\Users\Erica Rafael\Desktop\python full\python + Banco de Dados\arquivos\update_value.txt'), 'r') as arq:
        lines = arq.readlines()

    lines = list(map(lambda x: x.replace("\n", ""), lines))
    tabela = lines[0].replace("TABELA: ", "")
    coluna = lines[1].replace("COLUNA A SER ATUALIZADA: ", "")
    valor = lines[2].replace("NOVO VALOR DA COLUNA: ", "")
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"DELETE FROM {tabela} WHERE {coluna} = '{valor}'")
            print(f"DELETE FROM {tabela} WHERE {coluna} = '{valor}'")
    except Exception as e:
        print(f"Error: {e}")

# delete_data()
