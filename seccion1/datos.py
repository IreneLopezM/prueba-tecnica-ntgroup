def extraer_datos(archivo_csv):
    datos_csv = []

    try:
        #Se abre y se extraen los datos del archivo csv en una lista.
        with open(archivo_csv, "r") as csv:
            datos_csv = csv.read().splitlines()

        return datos_csv
    
    except:
        print("Error en la extracción de datos.")