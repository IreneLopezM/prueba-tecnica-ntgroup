import mysql.connector

def cargar(datos_csv):
    errores = []

    try:
        #Conexion a la base de datos
        db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "nt_group"
        )
        db_cursor = db.cursor()

        for dato_csv in datos_csv:
            if dato_csv != ",,,,,," and dato_csv != "id,name,company_id,amount,status,created_at,paid_at":
                aux_dato_csv = dato_csv.split(",")

                if aux_dato_csv[0] and aux_dato_csv[2] and aux_dato_csv[3] and aux_dato_csv[4] and aux_dato_csv[5]:
                    #Insertar datos a la tabla companies
                    try:
                        sql = "INSERT IGNORE INTO companies VALUES(%s, %s)"
                        val = (aux_dato_csv[2], aux_dato_csv[1]) #company_id, name
                        
                        db_cursor.execute(sql, val)
                        db.commit()

                    except:
                        print("Error al insertar datos en la tabla companies.")
                        errores.append(aux_dato_csv)

                    #Insertar datos a la tabla charges
                    try:
                        #A created_at se le da el formato "yyyy-mm-dd 00:00:00"
                        hora = "00:00:00"
                        if "T" in aux_dato_csv[5]:
                            aux = aux_dato_csv[5].split("T")
                            fecha = aux[0].split("/")
                            hora = aux[1]

                        else:
                            fecha = aux_dato_csv[5].split("/")
                        date_created = f"{fecha[2]}-{fecha[1]}-{fecha[0]} {hora}"

                        #A amount se le da el formato float con 2 decimales 
                        amount = "{:.2f}".format(float(aux_dato_csv[3]))

                        #A updated_at se le da el formato "yyyy-mm-dd 00:00:00"
                        if aux_dato_csv[6]: #Primero se verifica que hay un update_at
                            if "T" in aux_dato_csv[6]:
                                aux = aux_dato_csv[6].split("T")
                                fecha = aux[0].split("/")
                                hora = aux[1]

                            else:
                                fecha = aux_dato_csv[6].split("/")
                            date_update = f"{fecha[2]}-{fecha[1]}-{fecha[0]} {hora}" 

                            sql = "INSERT INTO charges VALUES(%s, %s, %s, %s, %s, %s)"
                            val = (aux_dato_csv[0], aux_dato_csv[2], amount, aux_dato_csv[4], date_created, date_update) #id, company_id, amount, status, created_at, update_at

                        else: #De lo contrario solo se insertan los otros datos
                            sql = "INSERT INTO charges (id, company_id, amount, status, created_at) VALUES(%s, %s, %s, %s, %s)"
                            val = (aux_dato_csv[0], aux_dato_csv[2], float(aux_dato_csv[3]), aux_dato_csv[4], date_created)#id, company_id, amount, status, created_at
                        
                        db_cursor.execute(sql, val)
                        db.commit()

                    except:
                        print(f"Error al insertar datos en la tabla charges.")
                        errores.append(aux_dato_csv)

                else:
                    errores.append(aux_dato_csv)

        #Cerrar canales de comunicación con la db
        db_cursor.close()
        db.close()
    
    except:
        print("Fallo la conexión con la base de datos.")


    #Se crea un archivo csv que contendra los errores encontrados
    try:
        with open("errores.csv", "w+", encoding="utf-8") as errores_csv:
            errores_csv.write("id,name,company_id,amount,status,created_at,paid_at\n")
            for error in errores:
                aux_error = ",".join(error)
                errores_csv.write(str(aux_error) + "\n")

    except:
        print("Ocurrió un error en el archivo errores.csv")


            
