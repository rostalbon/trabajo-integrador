from robot import Robot

class robotLimpieza(Robot):
    def __init__(self, nombre, color, onOff=False, escoba=True, aspiradora=True, trapeadora=True):
        super().__init__(nombre, color, onOff)
        self._escoba = escoba
        self._aspiradora = aspiradora
        self._trapeadora = trapeadora

    def get_esoba(self):
        if self._escoba:
            return "La escoba esta guardada"
        else:
            return "El robot está barriendo"
    
    def barrer(self):
        if self._escoba == False:
            self._escoba = True
            return f"{self._nombre} dejó de barrer"
        elif self._escoba and self._escoba and self._trapeadora:
            self._escoba = False
            return f"{self._nombre} está barriendo"
        else:
            return "El robot está ocupado con otra tarea"
        
    def aspirar(self):
        if self._aspiradora == False:
            self._aspiradora = True
            return f"{self._nombre} dejó de aspirar"
        else:
            return f"{self._nombre} está aspirando"
        
    def trapea(self):
        if self._trapeadora == False:
            self._aspiradora=True
            return f"{self._nombre} dejó de trapear"
        else:
            return f"{self._nombre} está trapeando"    