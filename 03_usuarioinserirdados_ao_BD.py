import mysql.connector
from mysql.connector import Error

print("Rotina para cadastro de produtos no banco de dados")
print("Entre com os dados conforme solicitados")

#Vou criar variaveis para armazenar os valores que irão para o BD
idProd = input("ID do Produto: ")
nomeProd = input("Nome do produto: ")
precoProd = input("Preço: ")
quantProd = input("Quantidade: ")


try:
    #Conectando ao banco de dados
    con = mysql.connector.connect(host = "localhost",
                                  database = "db_biblioteca",
                                  user = "root",
                                  password = "#Lucas10112")

    #Iserir registros ao BD

    inserir_produtos = f"""INSERT INTO tbl_produtos 
                                (IdProduto, NomeProduto, Preco, Quantidade)
                            VALUES
                            ({idProd},'{nomeProd}',{precoProd},{quantProd})
                        
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
