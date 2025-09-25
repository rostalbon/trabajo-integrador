from robot import Robot

class Niñero(Robot):
    def __init__(self, nombre, color, mamadera=True, articulosLimpieza=True, arropar=True):
        super().__init__(nombre, color)
        self._mamadera = mamadera
        self._articulosLimpieza = articulosLimpieza
        self._arropar = arropar

    def get_trabajo(self):
        if self._mamadera == True and self._articulosLimpieza == True and self._arropar == True:
            return f"{self._nombre} no está trabajando"
        elif self._mamadera == False:
            return f"{self._nombre} está dando la mamadera"
        elif self._articulosLimpieza == False:
            return f"{self._nombre} está limpiando"
        else:
            return f"{self._nombre} está arropando"
    
    def limpiar(self):
        if self._articulosLimpieza == True and self._mamadera == True and self._arropar == True:
            self._articulosLimpieza = False
            return f"{self._nombre} está limpiando"
        elif self._articulosLimpieza == False:
            self._articulosLimpieza = True
            return f"{self._nombre} dejó de limpiar"
        else:
            return f"{self._nombre} está haciendo otro trabajo, deja de hacerlo para limpiar"
    
    def darMamadera(self):
        if self._mamadera == True and self._arropar == True and self._articulosLimpieza == True:
            self._mamadera = False
            return f"{self._nombre} está dando la mamadera"
        elif self._mamadera == False:
            self._mamadera = True
            return f"{self._nombre} ya no está dando la mamadera"
        else:
            return f"{self._nombre} está haciendo otro trabajo, deja de hacerlo para dar la mamadera"
    
    def arropar(self):
        if self._mamadera == True and self._arropar == True and self._articulosLimpieza == True:
            self._arropar = False
            return f"{self._nombre} está arropando"
        elif self._arropar == False:
            self._arropar = True
            return f"{self._nombre} ya no está arropando"