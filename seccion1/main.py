import sys
from datos import extraer_datos
from crear_db import crear
from cargar_datos import cargar

#Se manda a llamar a la función que crea la db
crear()

try:
    #Se manda a llamar a la función que extrae los datos y se le pasa como parámetro el archivo csv
    datos_csv = extraer_datos(str(sys.argv[1]))

    #Se cargan los datos en db
    cargar(datos_csv)
    
except:
    print("Error al ingresar el archivo csv, verifique que sea correcto")