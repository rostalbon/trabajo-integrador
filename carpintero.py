from robot import Robot

class Carpintero(Robot):
    def __init__(self, nombre, color, onOff=False, hacha=False, sierra=False, destornillador=False):
        super().__init__(nombre, color, onOff)
        self._hacha = hacha
        self._sierra = sierra
        self._destornillador = destornillador

    def hachar(self):
        if self._hacha:
            self._hacha = False
            return f"{self._nombre} dejó de usar el hacha"
        else:
            self._hacha = True
            return f"{self._nombre} está hachando madera"

    def cerruchar(self):
        if self._sierra:
            self._sierra = False
            return f"{self._nombre} dejó de usar la sierra"
        else:
            self._sierra = True
            return f"{self._nombre} está cerruchando madera"

    def atornillar(self):
        if self._destornillador:
            self._destornillador = False
            return f"{self._nombre} dejó de atornillar"
        else:
            self._destornillador = True
            return f"{self._nombre} está atornillando"

    def desatornillar(self):
        if self._destornillador:
            self._destornillador = False
            return f"{self._nombre} dejó de desatornillar"
        else:
            self._destornillador = True
            return f"{self._nombre} está desatornillando"