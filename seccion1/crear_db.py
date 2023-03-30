import mysql.connector

def crear():
    try:
        #Se establece la conexión
        db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root"
        )

        #Se crear un cursor
        db_cursor = db.cursor()

        #Con el cursor verifico primero que no exista la base, de lo contrario la elimina
        db_cursor.execute("DROP DATABASE IF EXISTS nt_group")
        #Se crea la base de datos
        db_cursor.execute("CREATE DATABASE nt_group")

        #Se selecciona la base creada 
        db_cursor.execute("USE nt_group")

        #Se crea la tabla para las compañias 
        db_cursor.execute("""CREATE TABLE companies (
            company_id varchar(40) NOT NULL PRIMARY KEY,
            company_name varchar(130) NULL UNIQUE
            )""")
        #Se crea la tabla para las transacciones 
        db_cursor.execute("""CREATE TABLE charges (
            id varchar(40) NOT NULL PRIMARY KEY,
            company_id varchar(40) NOT NULL,
            amount decimal(16,2) NOT NULL,
            status varchar(30) NOT NULL,
            created_at timestamp NOT NULL,
            updated_at timestamp NULL,
            FOREIGN KEY (company_id) REFERENCES companies(company_id)
            )""")
        
        #Cerrar canales de comunicación con la db
        db_cursor.close()
        db.close()

    except:
        print("Ocurrió un error en la creación de la base de datos.")