from robot import Robot

class Cocinero(Robot):
    def __init__(self, nombre, color, batidora, cuchillo, cuchara, microfono=True, parlante=True, onOff=False):
        super().__init__(nombre, color, microfono, parlante, onOff)
        self._batidora = batidora
        self._cuchillo = cuchillo
        self._cuchara = cuchara
    