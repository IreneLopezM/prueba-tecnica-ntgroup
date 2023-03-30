import sys
from generar_numeros import generar
from clase import Conjuntos

#Se comprueba que el valor ingresado este dentro del rango.
if int(sys.argv[1]) >= 0 and int(sys.argv[1]) < 100:

    #Se generan los 100 primeros números naturales.
    num = generar()
    #Se crea el objeto que contendra los números, pasando como parámetro los números anteriormente generados.
    num_obj = Conjuntos(num)


    #Se extrae el número que el usuario ingreso.
    num_obj.extract(int(sys.argv[1]))

    #Se busca el número extraído.
    num_obj.search()

else:
    print("Ingrese un número valido dentro del rango.")