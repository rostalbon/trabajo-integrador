class Robot:
    def __init__(self, nombre, color, microfono=0, parlante=0, onOff=0):
        self._color = color
        self._microfono = microfono
        self._parlante = parlante
        self._nombre = nombre
        self._onOff = onOff

    def encender(self):
        self._onOff = 1
        return f"{self._nombre} está encendido"

    def apagar(self):
        self._onOff = 0
        return f"{self._nombre} está apagado"

    def mover(self):
        return f"{self._nombre} se movió correctamente"