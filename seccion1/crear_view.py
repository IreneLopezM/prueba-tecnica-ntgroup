import mysql.connector
import sys

def view(id_company, date_created):
    try: 
        #Conexion a la base de datos
        db = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "root",
                database = "nt_group"
            )
        db_cursor = db.cursor()

        try:
            #Creación de la plantilla de view para mostrar el total transaccionado de cierta empresa en cierto día.
            sql = "CREATE OR REPLACE VIEW total_paid_vw AS SELECT SUM(amount) AS total_paid FROM charges WHERE company_id = %s AND created_at = %s AND status = 'paid'"
            val = (id_company, date_created) #company_id, created_at
            
            db_cursor.execute(sql, val)
            db.commit()
            
            #Muestra el resultado de la view
            db_cursor.execute("SELECT total_paid FROM total_paid_vw")
            view_resultado = str(db_cursor.fetchall()).split("'")
            
            print(f"Total facturado: {view_resultado[1]}")

        except:
            print("Error: Los datos ingresados son incorrectos.")

        #Cerrar canales de comunicación con la db.
        db_cursor.close()
        db.close()
    
    except:
        print("Fallo la conexión con la base de datos.")


#Manda a llamar a la función y le pasa el id de una empresa y la fecha de creación de la transacción.
view(str(sys.argv[1]), str(sys.argv[2]))