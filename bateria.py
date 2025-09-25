class Bateria:
    def __init__(self, porcentaje=100):
        self._porcentaje = porcentaje
    def get_porcentaje(self):
        return self._porcentaje
    def set_porcentaje(self, porcentaje):
        self._porcentaje = porcentaje
        return f"El porcentaje de batería actual es {self._pocentaje}%"