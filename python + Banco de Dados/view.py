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

# inserindo dados
