class Robot:
    def __init__(self, nombre, color, microfono=0, parlante=0):
        self.__color = color
        self.__microfono = microfono
        self.__parlante = parlante
        self.__nombre = nombre

    def encender(self):
        return f"{self.__nombre} esta encendido"

    def apagar(self):
        return f"{self.__nombre} esta apagado"

    def mover(self):
        return f"{self.__nombre} se movio correctamente"