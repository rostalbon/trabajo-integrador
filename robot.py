class Robot:
    def __init__(self, nombre, color, microfono=0, parlante=0):
        self._color = color
        self._microfono = microfono
        self._parlante = parlante
        self._nombre = nombre

    def encender(self):
        return f"{self._nombre} esta encendido"

    def apagar(self):
        return f"{self._nombre} esta apagado"

    def mover(self):
        return f"{self._nombre} se movio correctamente"