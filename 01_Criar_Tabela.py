import mysql.connector

try:
    #Criar conexão ao banco de dados
    con = mysql.connector.connect(host = "localhost",
                                  database = "db_biblioteca",
                                  user = "root",
                                  password = "#Lucas10112")
    #Declaração SQL a ser executada
    criar_tabela = """CREATE TABLE tbl_produtos (
                         IdProduto int(11) NOT NULL,
                         NomeProduto VARCHAR(70) NOT NULL,
                         preco FLOAT NOT NULL,
                         Quantidade TINYINT NOT NULL,
                         PRIMARY KEY (IdProduto)) """
    #Criar cursos para executar SQL no banco de dados
    cursor = con.cursor()
    cursor.execute(criar_tabela)
    print("Tabela de produtos criada com sucesso!")
except mysql.connector.Error as erro:
    print(f"Falha ao criar tabela no MySQL: {erro}")
finally:
    if (con.is_connected()):
        cursor.close()
        con.close()
        print("Conexão ao MySQL finalizada")

