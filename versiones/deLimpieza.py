from robot import Robot

class robotLimpieza(Robot):
    def __init__(self, nombre, color, microfono=True, parlante=True, onOff=False, escoba=True, aspiradora=True, trapeadora=True):
        super().__init__(nombre, color, microfono, parlante, onOff)
        self._escoba = escoba
        self._aspiradora = aspiradora
        self._trapeadora = trapeadora
    
    def barrer(self):
        if self._escoba == False:
            self._escoba = True
            return f"{self._nombre} dejo de barrer"
        else:
            return f"{self._nombre} está barriendo"
        
    def aspirar(self):
        if self._aspiradora:
            return f"{self._nombre} está aspirando"
        else:
            return f"{self._nombre} no tiene la aspiradora disponible"
    def trapea(self):
        if self._trapeadora:
            return f"{self._nombre} está trapeando"
        else:
            return f"{self._nombre} no tiene el trapeador disponible en este momento"    