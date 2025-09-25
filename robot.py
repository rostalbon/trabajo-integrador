from bateria import Bateria

class Robot:
    def __init__(self, nombre, color, accesorios=[]):
        self._color = color
        self._nombre = nombre
        self._accesorios = accesorios
        self._porcentaje = Bateria()

    def get_accesorios_array(self):
        return self._accesorios

    def get_accesorios(self):
        if self._accesorios == []:
            return f"{self._nombre} no está usando accesorios"
        else:
            res = ""
            for accesorio in self._accesorios:
                if res == "":
                    res = accesorio
                else:
                    res = res + f", {accesorio}"
            return res
    
    def agregar_accesorio(self, accesorio):
        self._accesorios.append(accesorio)
        return f"Se añadió {accesorio} a la lista de accesorios"
    
    def eliminar_accesorio(self, num):
        res = self._accesorios[num]
        self._accesorios.remove(num)
        return f"{res} se eliminó correctamente de la lista de accesorios"

    def get_bateria(self):
        return self._porcentaje.get_porcentaje()

    def set_bateria(self, bateria):
        self._porcentaje = Bateria(bateria)
        return f"Se actualizó el porcentaje de batería a {self._porcentaje.get_porcentaje()}%"

    def get_nombre(self):
        return self._nombre
    
    def get_color(self):
        return self._color

    def encender(self):
        self._onOff = 1
        return f"{self._nombre} está encendido"

    def apagar(self):
        self._onOff = 0
        return f"{self._nombre} está apagado"

    def mover(self):
        return f"{self._nombre} se movió correctamente"