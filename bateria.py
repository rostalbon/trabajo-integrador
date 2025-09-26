class Bateria:
    def __init__(self, porcentaje=100):
        self._porcentaje = porcentaje
    def get_porcentaje(self):
        return self._porcentaje