from robot import Robot

class Carpintero(Robot):
    def __init__(self, nombre, color, microfono=True, parlante=True, onOff=False, hacha=False, sierra=False, destornillador=False):
        super().__init__(nombre, color, microfono, parlante, onOff)
        self._hacha = hacha
        self._sierra = sierra
        self._destornillador = destornillador