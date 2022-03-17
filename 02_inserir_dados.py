import mysql.connector
from mysql.connector import Error

try:
    #Conectando ao banco de dados
    con = mysql.connector.connect(host = "localhost",
                                  database = "db_biblioteca",
                                  user = "root",
                                  password = "#Lucas10112")

    #Iserir registros ao BD

    inserir_produtos = """INSERT INTO tbl_produtos 
                                (IdProduto, NomeProduto, Preco, Quantidade)
                            VALUES
                            (1,'Câmera',850.00,5),
                            (2,'Monitor',630.00,7),
                            (3,'Relógio',575.00,10)
                            """

    cursor = con.cursor()
    cursor.execute(inserir_produtos)
    con.commit()
    print(f"{cursor.rowcount} Registros Inseridos na tabela")
    cursor.close()
except Error as erro:
    print(f"Falha ao inserir dados no MySQL: {erro}")
finally:
    if (con.is_connected()):
        cursor.close()
        con.close()
        print("Conexão ao MYSQL finalizada")
