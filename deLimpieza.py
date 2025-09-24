from robot import Robot

class robotLimpieza(Robot):
    def __init__(self, nombre, color, onOff=False, escoba=True, aspiradora=True, trapeadora=True):
        super().__init__(nombre, color, onOff)
        self._escoba = escoba
        self._aspiradora = aspiradora
        self._trapeadora = trapeadora

    def get_escoba(self):
        if self._escoba:
            return "La escoba esta guardada"
        else:
            return "El robot está barriendo"
        
    def get_aspiradora(self):
        if self._aspiradora:
            return "La aspiradora está apagada"
        else:
            return "El robot está aspirando" 

    def get_trapeadora(self):
        if self._trapeadora:
            return "El trapeador está guardado"
        else:
            return "El robot está trapeando"   
    
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
        elif self._aspiradora and self._escoba and self._trapeadora:
            self._aspiradora = False
            return f"{self._nombre} está aspirando"
        else:
            return "El robot está ocupado"
        
    def trapea(self):
        if self._trapeadora == False:
            self._aspiradora=True
            return f"{self._nombre} dejó de trapear"
        elif self._trapeadora and self._escoba and self._aspiradora:
            self._trapeadora = False
            return f"{self._nombre} está trapeando"   
        else:
            return "El robot está ocupado"