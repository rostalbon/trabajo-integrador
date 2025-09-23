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
            return f"{self._nombre} dejó de batir"
        else:
            self._batidora = False
            return f"{self._nombre} está batiendo"
    def revolver(self):
        if self._cuchara == False:
            self._cuchara = True
            return f"{self._nombre} dejó de revolver"
        else:
            self._cuchara = False
            return f"{self._nombre} está revolviendo"
    def cortar(self):
        if self._cuchillo == False:
            self._cuchillo = True
            return f"{self._nombre} dejó de cortar"
        else:
            self._cuchillo = False
            return f"{self._nombre} está cortando"