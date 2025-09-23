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
            return f"{self._nombre} dejó de barrer"
        else:
            return f"{self._nombre} está barriendo"
        
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