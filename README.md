# Prueba Técnica NT-Group

## INDICE 
1.	Procesamiento y transferencia de datos
    * 1.1.	Lenguaje de programación y herramientas.
    * 1.2.	 Instalación del entorno
    * 1.3.	 Ejecución del proyecto en Windows
2.	Creación de una API
    * 2.1.	 Ejecución del proyecto en Windows
    
<br>

## 1.	Procesamiento y transferencia de datos
### 1.1	 Lenguaje de programación y herramientas.
Este proyecto está desarrollado en: 
* Python
* MySQL
* CSV

#### ¿Por qué los elegí?
Elegí Python porque es el lenguaje que más domino y por el cual estoy aplicando a esta vacante.

Para extraer los datos proporcionados en el archivo de Excel elegí usar el formato CSV porque es fácil de transformar un archivo Excel a CSV, además de que es muy sencillo de usar y modificar.

Por último, use MySQL para crear la base de datos porque es un gestor de bases de datos que conozco bastante bien y con el que me siento más cómoda. 

#### ¿Qué retos encontré? 
En este proyecto encontré dos retos:

El primero fue que en algunas transacciones no estaban datos que no podían ser nulos, por lo cual recolecte todas esas transacciones y genere un archivo CSV donde se guardaron para que posteriormente la persona que se encargó de llenar el documento en Excel revise este documento y corrija los errores para poder volverlo a cargar a la base de datos.

El segundo reto fue que tuve que modificar el esquema para la información porque el tamaño de los ID era más grande. 

### 1.2.	Instalación del entorno
Antes de ejecutar el código, debes de instalar lo siguiente:
* [Python 3.8 64bits](https://www.python.org/downloads/)
* [MySQL Server 8.0](https://dev.mysql.com/downloads/installer/)

### 1.3.	 Ejecución del proyecto en Windows
El proyecto se encuentra dentro de la carpeta “seccion1”.
1.	Abre el CMD dentro de la carpeta 
2.	Ejecuta el siguiente comando `python main.py data_prueba_tecnica.csv`
    * Si tienes otro archivo csv que cumpla con el formato del archivo “data_prueba_tecnica.csv” puedes ingresarlo en su lugar.
    * Si ya cargaste el archivo “data_prueba_tecnica.csv” y deseas cargar más datos solo debes comentar la línea que dice “crear()” en el archivo main.py y ejecutar el comando nuevamente con la ruta del archivo que deseas cargar.
3.	Para crear una view ejecuta el siguiente comando: `python crear_view.py id_company date_created`
    * Reemplaza id_company por el ID de la empresa de la cual deseas saber el total de transacciones.
    * Reemplaza date_created por el día del cual deseas saber el total de transacciones. (**IMPORTANTE:** usa este formato para la fecha yyyy-mm-dd 00:00:00)
    * Ejemplo: `python crear_view.py cbf1c8b09cd5b549416d49d220a40cbd317f952e 2019-02-03 00:00:00`

<br>

## 2.	Creación de una API
### 2.1.	 Ejecución del proyecto en Windows
El proyecto se encuentra dentro de la carpeta “seccion2”.
1.	Abre el CMD dentro de la carpeta 
2.	Ejecuta el siguiente comando `python main.py numero`
    * Reemplaza numero por el número que deseas extraer. (**IMPORTANTE:** el número debe de estar dentro del rango 0 al 99)
    * Ejemplo: `python main.py 89`
