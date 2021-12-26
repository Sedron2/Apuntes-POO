class Coordenada:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def distancia(self, otro_punto):
        return ((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)**0.5


punto1 = Coordenada(0, 0)
punto2 = Coordenada(7, 24)

print(punto1.distancia(punto2))