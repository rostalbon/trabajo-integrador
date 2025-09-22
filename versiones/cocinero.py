from robot import Robot

class Cocinero(Robot):
    def __init__(self, nombre, color, batidora=False, cuchillo=False, cuchara=False, microfono=True, parlante=True, onOff=False):
        super().__init__(nombre, color, microfono, parlante, onOff)
        self._batidora = batidora
        self._cuchillo = cuchillo
        self._cuchara = cuchara
    def batir(self):
        if self._batidora == True:
            self._batidora = False
            return "Se desactivó la batidora"
        else:
            self._batidora = True
            return "Se activó la batidora"
    def revolver(self):
        if self._cuchara == True:
            self._cuchara = False
            return "Se desactivó la cuchara"
        else:
            self._cuchara = True
            return "Se activó la cuchara"
    def cortar(self):
        if self._cuchillo == True:
            self._cuchillo = False
            return "Se desactivó el cuchillo"
        else:
            self._cuchillo = True
            return "Se activó el cuchillo"