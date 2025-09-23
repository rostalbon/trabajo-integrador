from robot import Robot

class Cocinero(Robot):
    def __init__(self, nombre, color, batidora=True, cuchillo=True, cuchara=True, microfono=True, parlante=True, onOff=False):
        super().__init__(nombre, color, microfono, parlante, onOff)
        self._batidora = batidora
        self._cuchillo = cuchillo
        self._cuchara = cuchara
    def batir(self):
        if self._batidora == False:
            self._batidora = True
            return "Se desactivó la batidora"
        else:
            self._batidora = False
            return "Se activó la batidora"
    def revolver(self):
        if self._cuchara == False:
            self._cuchara = True
            return "Se desactivó la cuchara"
        else:
            self._cuchara = False
            return "Se activó la cuchara"
    def cortar(self):
        if self._cuchillo == False:
            self._cuchillo = True
            return "Se desactivó el cuchillo"
        else:
            self._cuchillo = False
            return "Se activó el cuchillo"