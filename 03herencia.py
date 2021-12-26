class Cuadrilátero:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura


    @property
    def area(self):
        return self.base * self.altura


    @property
    def perímetro(self):
        return 2*self.base + 2*self.altura


class Cuadrado(Cuadrilátero):

    def __init__(self, lado):
        super().__init__(lado, lado)



rectangulo = Cuadrilátero(3, 4)

print(rectangulo.area)

cuadrado = Cuadrado(5)

print(cuadrado.area, cuadrado.perímetro)