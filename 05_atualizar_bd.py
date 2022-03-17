import mysql.connector
from mysql.connector import Error

#Atualizar registros em um banco de dados MySQL

def conectar():
    try:
        global con
        con = mysql.connector.connect(host = "localhost",
                                      database = "db_biblioteca",
                                      user = "root",
                                      password = "#Lucas10112")
    except Error as erro:
        print(f"Erro de conexão: {erro}")

def inserir(idProd,nomeProd,precoProd,quantProd):
    conectar()
    insere = f"""INSERT INTO tbl_produtos (IdProduto, NomeProduto, Preco, Quantidade)
                            VALUES
                            ({idProd},'{nomeProd}',{precoProd},{quantProd})"""
    cursor = con.cursor()
    cursor.execute(insere)
    con.commit()
    print(f"{cursor.rowcount} Registros Inseridos na tabela")

def consulta(idProd):
    try:
        conectar()
        consulta_sql = f'select * from tbl_produtos WHERE IdProduto = {idProd}'
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        for linha in linhas:
            print(f"Id: {linha[0]}\n"
                  f"Produto: {linha[1]}\n"
                  f"Preço: {linha[2]}\n")

    except Error as erro:
        print(f"Falha ao consultar a tabela: {erro}")
    finally:
        if(con.is_connected()):
            cursor.close()
            con.close()

def atualiza(declaracao):
    try:
        conectar()
        altera_preco = declaracao
        cursor = con.cursor()
        cursor.execute(altera_preco)
        con.commit()
        print("Preço alterado com sucesso")

    except Error as erro:
        print(f"Falha ao inserir dados na tabela: {erro}")
    finally:
        if(con.is_connected()):
            cursor.close()
            con.close()


def deleta(idProd):
    conectar()
    deleta = f"DELETE FROM tbl_produtos WHERE idProduto = {idProd}"
    cursor = con.cursor()
    cursor.execute(deleta)
    con.commit()


#Essa linha indica onda o programa vai iniciar efetivamente
if __name__ =='__main__':
    print("Atualizar preços de produtos no banco de dados")
    print("Entre com os dados solicitados:")
    print(f"\nDigite o código do produto para alterar: ")
    idProd = input("ID do produto: ")
    nomeProd = input("Nome do Produto: ")
    precoProd = input("Preço do Produto: ")
    quantProd = input("Quantidade do produto: ")

    inserir(idProd,nomeProd,precoProd,quantProd)

    consulta(idProd)
    
    '''print("\nEntre com o novo preço do produto:")
    precoProd = input("Preço: ")

    declaracao = f"""UPDATE tbl_produtos
    SET preco = {precoProd} WHERE IdProduto = {idProd}"""
    print(declaracao)

    atualiza(declaracao)'''
    
    verifica = input("\nDeseja consultar a atualização? s = sim, n = não: ").upper()
    if verifica in "S":
        consulta(idProd)
    else:
        print("\nAté mais!")

