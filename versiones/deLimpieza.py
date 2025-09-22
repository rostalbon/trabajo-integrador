from robot import Robot

class robotLimpieza(Robot):
    def __init__(self, nombre, color, microfono=True, parlante=True, onOff=False, escoba=False, aspiradora=False, trapeadora=False):
        super().__init__(nombre, color, microfono, parlante, onOff)
        self._escoba = escoba
        self._aspiradora = aspiradora
        self._trapeadora = trapeadora
    