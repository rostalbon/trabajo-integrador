from robot import Robot

class RobotLimpieza(Robot):
    def __init__(self, nombre, color, escoba=True, aspiradora=True, trapeadora=True):
        super().__init__(nombre, color)
        self._escoba = escoba
        self._aspiradora = aspiradora
        self._trapeadora = trapeadora

    def get_trabajo(self):
        if self._escoba == True and self._aspiradora == True and self._trapeadora == True:
            return f"{self._nombre} no está trabajando"
        elif self._escoba == False:
            return f"{self._nombre} está barriendo"
        elif self._aspiradora == False:
            return f"{self._nombre} está aspirando"
        else:
            return f"{self._nombre} está trapeando"   
    
    def barrer(self):
        if self._escoba == False:
            self._escoba = True
            return f"{self._nombre} dejó de barrer"
        elif self._escoba and self._escoba and self._trapeadora:
            self._escoba = False
            return f"{self._nombre} está barriendo"
        else:
            return f"{self._nombre} está haciendo otro trabajo, deja de hacerlo para barrer"
        
    def aspirar(self):
        if self._aspiradora == False:
            self._aspiradora = True
            return f"{self._nombre} dejó de aspirar"
        elif self._aspiradora and self._escoba and self._trapeadora:
            self._aspiradora = False
            return f"{self._nombre} está aspirando"
        else:
            return f"{self._nombre} está haciendo otro trabajo, deja de hacerlo para aspirar"
        
    def trapear(self):
        if self._trapeadora == False:
            self._aspiradora=True
            return f"{self._nombre} dejó de trapear"
        elif self._trapeadora and self._escoba and self._aspiradora:
            self._trapeadora = False
            return f"{self._nombre} está trapeando"   
        else:
            return f"{self._nombre} está haciendo otro trabajo, deja de hacerlo para trapear"