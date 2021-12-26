import time

class Lavadora:

    def __init__(self):
        pass


    def lavar(self, temperatura='caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._añadir_jabon()
        self._lavar()
        self._centrifugar()
        self._avisar()


    def _llenar_tanque_de_agua(self, temperatura):
        print('Llenando el tanque con agua ' + temperatura)
        time.sleep(1)


    def _añadir_jabon(self):
        print('Añadiendo jabón')
        time.sleep(1)


    def _lavar(self):
        print('Lavando la ropa')
        time.sleep(1)

    
    def _centrifugar(self):
        print('Centrifugando la ropa')
        time.sleep(1)


    def _avisar(self):
        print('Ya está lista la ropa!')


miLavadora = Lavadora()

miLavadora.lavar()