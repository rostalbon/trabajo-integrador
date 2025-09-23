from robot import Robot

class niñero(Robot):
    def __init__(self, nombre, color, mamadera=False, articulosLimpieza=False, microfono=True, parlante=True, onOff=False):
        super().__init__(nombre, color, microfono, parlante, onOff)
        self._mamadera=mamadera
        self._articulosLimpieza=articulosLimpieza

    def limpiar(self):
        if self._articulosLimpieza==True:
            print("El robot está limpiando")