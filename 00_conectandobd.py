import mysql.connector

con = mysql.connector.connect(host = "localhost", database = "db_biblioteca", user = "root", password = "#Lucas10112")

if con.is_connected():
    #Pega informações do servidor
    db_info = con.get_server_info()
    print(f"Conectado ao servidor MySQL versão {db_info}")

    #Cria um cursor
    cursor = con.cursor()
    #Seleciona a banco de dados atual
    cursor.execute("select database();")
    #Retorna uma linha desde banco de dados
    linha = cursor.fetchone()
    print(f"Conectado ao banco de dados {linha}")

if con.is_connected():
    cursor.close()
    con.close()
    print("A conexão ao MySQL foi encerrada")