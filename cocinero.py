from robot import Robot

class Cocinero(Robot):
    def __init__(self, nombre, color, batidora=True, cuchillo=True, cuchara=True, onOff=False):
        super().__init__(nombre, color, onOff)
        self._batidora = batidora
        self._cuchillo = cuchillo
        self._cuchara = cuchara
    def get_trabajo(self):
        if self._batidora == True and self._cuchillo == True and self._cuchara == True:
            return "El robot no está trabajando"
        elif self._batidora == False:
            return "El robot está batiendo"
        elif self._cuchillo == False:
            return "El robot está cortando"
        else:
            return "El robot está revolviendo"
    def batir(self):
        if self._batidora == False:
            self._batidora = True
            return f"{self._nombre} dejó de batir"
        elif self._batidora == True and self._cuchillo == True and self._cuchara == True:
            self._batidora = False
            return f"{self._nombre} está batiendo"
        else:
            f"{self._nombre} está haciendo otro trabajo, deja de hacerlo para batir"
    def revolver(self):
        if self._cuchara == False:
            self._cuchara = True
            return f"{self._nombre} dejó de revolver"
        elif self._cuchara == True and self._cuchillo == True and self._batidora == True:
            self._cuchara = False
            return f"{self._nombre} está revolviendo"
        else:
            f"{self._nombre} está haciendo otro trabajo, deja de hacerlo para batir"
    def cortar(self):
        if self._cuchillo == False:
            self._cuchillo = True
            return f"{self._nombre} dejó de cortar"
        elif self._cuchillo == True and self._batidora == True and self._cuchara == True:
            self.cuchillo = False
            return f"{self._nombre} está cortando"
        else:
            f"{self._nombre} está haciendo otro trabajo, deja de hacerlo para batir"