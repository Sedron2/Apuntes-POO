class Hotel:
    
    def __init__(self, numero_maximo_de_huespedes, lugares_de_estacionamiento):
        self.numero_maximo_de_huespedes = numero_maximo_de_huespedes
        self.lugares_de_estacionamiento = lugares_de_estacionamiento
        self.huespedes = 0


    def añadir_huespedes(self, numero):
        self.huespedes += numero

    
    def ampliar_hotel(self, numero):
        self.numero_maximo_de_huespedes += numero


    def ampliar_estacionamiento(self, numero):
        self.lugares_de_estacionamiento += numero


cuarto = Hotel(50, 20)

cuarto.añadir_huespedes(4)
cuarto.ampliar_estacionamiento(15)


print(cuarto.huespedes, cuarto.lugares_de_estacionamiento, type(cuarto))
print(vars(cuarto), dir(cuarto))
