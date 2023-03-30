class Conjuntos():
    def __init__(self, numeros_list):
        self.numeros = numeros_list #primeros 100 números naturales

    def extract(self, ext_num):
        for numero in self.numeros:
            if numero == ext_num:
                self.numeros.remove(numero)

    def search(self):
        buscar_num = 0

        while buscar_num < 100:
            if not buscar_num in self.numeros:
                print(f"El número que se extrajo es: {buscar_num}")
                break
            
            buscar_num += 1
        