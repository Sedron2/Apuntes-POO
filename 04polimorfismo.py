class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    
    def avanzar(self):
        print('Caminando')


class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    
    def avanzar(self):
        return print('Pedaleando')


Sedron = Persona('Sedron')
Causa = Ciclista('Choche')

Sedron.avanzar()
Causa.avanzar()