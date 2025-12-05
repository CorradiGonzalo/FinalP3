continentes = ('0-America', '1-Europa', '2-Asia','3-Africa', '4-Oceania')

class Pais:
    def __init__(self, nombre, continente, oro, plata, bronce):
        self.nombre = nombre
        self.continente = continente
        self.oro = oro
        self.plata = plata
        self.bronce = bronce
        self.total = oro + plata + bronce

    def __str__(self):
        cad = 'Nombre: {:<10} | Continente: {:<10} | Oro: {:>3} | Plata: {:>3} | Bronce: {:>3} | Total: {:>3}'
        return cad.format(self.nombre, continentes[self.continente], self.oro, self.plata, self.bronce, self.total)

def prueba():
    p1 = Pais('Italia', 1, 14, 3, 4)
    p2 = Pais('Argentina', 0, 12, 3, 1)
    print(p1)
    print(p2)

if __name__ == '__main__':
    prueba()