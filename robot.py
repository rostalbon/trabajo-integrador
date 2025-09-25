from bateria import Bateria

class Robot:
    def __init__(self, nombre, color, bateria=100, microfono=True, parlante=True, onOff=False):
        self._color = color
        self._microfono = microfono
        self._parlante = parlante
        self._nombre = nombre
        self._onOff = onOff
        self._bateria = Bateria(bateria)

    def get_bateria(self):
        return self._bateria

    def set_bateria(self, bateria):
        self._bateria = Bateria(bateria)
        return f"Se actualizó el porcentaje de batería a {self._bateria}%"

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