from robot import Robot

class Carpintero(Robot):
    def __init__(self, nombre, color, onOff=False, hacha=True, sierra=True, destornillador=True):
        super().__init__(nombre, color, onOff)
        self._hacha = hacha
        self._sierra = sierra
        self._destornillador = destornillador

    def get_trabajo(self):
        if self._hacha and self._sierra and self._destornillador:
            return f"{self._nombre} no está trabajando"
        elif self._hacha == False:
            return f"{self._nombre} está usando el hacha"
        elif self._sierra == False:
            return f"{self._nombre} está usando la sierra"
        else:
            return f"{self._nombre} está usando el destornillador"

    def hachar(self):
        if self._hacha and self._sierra and self._destornillador:
            self._hacha = False
            return f"{self._nombre} está usando el hacha"
        elif self._hacha == False:
            self._hacha = True
            return f"{self._nombre} dejó de usar el hacha"
        else:
            return f"{self._nombre} está haciendo otro trabajo, deja de hacerlo para usar el hacha"

    def cerruchar(self):
        if self._sierra and self._hacha and self._destornillador:
            self._sierra = False
            return f"{self._nombre} está usando la sierra"
        elif self._sierra == False:
            self._sierra = True
            return f"{self._nombre} dejó de usar la sierra"
        else:
            return f"{self._nombre} está haciendo otro trabajo, deja de hacerlo para usar la sierra"
        
    def atornillar(self):
        if self._destornillador and self._hacha and self._sierra:
            self._destornillador = False
            return f"{self._nombre} está usando el destornillador"
        elif self._destornillador == False:
            self._destornillador = True
            return f"{self._nombre} dejó de usar el destornillador"
        else:
            return f"{self._nombre} está haciendo otro trabajo, deja de hacerlo para usar el destornillador"
