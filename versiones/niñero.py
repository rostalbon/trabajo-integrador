from robot import Robot

class niñero(Robot):
    def _init_(self, nombre, color, mamadera=False, articulosLimpieza=False, microfono=True, parlante=True, onOff=False):
        super()._init_(nombre, color, microfono, parlante, onOff)
        self._mamadera = mamadera
        self._articulosLimpieza = articulosLimpieza
    
    def limpiar(self):
        if self._articulosLimpieza==True:
            print("El robot está limpiando")
        else:
            print("¡El robot no tiene artículos de limpieza! Va a buscarlos.")
            self._articulosLimpieza=True
    
    def darMamadera(self):
        if self._mamadera==True:
            print("El robot está dandole la mamadera al niño.")
        else:
            print("¡El robot no encuentra la mamadera! Va a buscarla.")
            self._mamadera=True
    
    def arropar(self):
        print("El robot arropó al niño.")