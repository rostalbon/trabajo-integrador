from robot import Robot

class robotLimpieza(Robot):
    def __init__(self, nombre, color, microfono=True, parlante=True, onOff=False, escoba=False, aspiradora=False, trapeadora=False):
        super().__init__(nombre, color, microfono, parlante, onOff)
        self._escoba = escoba
        self._aspiradora = aspiradora
        self._trapeadora = trapeadora
    
    def barrer(self):
        if self._escoba:
            return f"{self._nombre} está barriendo"
        else:
            return f"{self._nombre} no cuenta con la escoba disponible"
        
    def aspirar(self):
        if self._aspiradora:
            return f"{self._nombre} está aspirando"
        else:
            return f"{self._nombre} no tiene la aspiradora disponible"
        