import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(host="localhost",
                                  database="db_biblioteca",
                                  user = "root",
                                  password = "#Lucas10112")

    consulta = "select * from tbl_produtos"
    cursor = con.cursor()
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    print(f"Numero total de registros retornados: {cursor.rowcount}")

    print("\nmostrar produtos cadastrados\n")
    for linha in linhas:
        print(f"Id do produto: {linha[0]}")
        print(f"Nome do produto: {linha[1]}")
        print(f"Preço: {linha[2]}")
        print(f"Quantidade: {linha[3]}\n")

except Error as e:
    print(f"Erro ao acessar tabela MySQL: {e}")
finally:
    if (con.is_connected()):
        cursor.close()
        con.close()
        print("Conexão ao MySQL encerrada")