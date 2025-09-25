from cocinero import Cocinero
from carpintero import Carpintero
from niñero import Niñero
from deLimpieza import RobotLimpieza

titulo_programa = "ROBOT"
print(f"╔═{"═" * len(titulo_programa)}═╗")
print(f"║ {" " * len(titulo_programa)} ║")
print(f"║ {titulo_programa} ║")
print(f"║ {" " * len(titulo_programa)} ║")
print(f"╚═{"═" * len(titulo_programa)}═╝")

print("~ DATOS DEL ROBOT ~")
nombre = input("Asígnele un nombre a su robot: ")
while True:
    print("¿De qué color quiere a su robot?")
    print("1. Rojo")
    print("2. Naranja")
    print("3. Amarillo")
    print("4. Verde")
    print("5. Azul")
    print("6. Violeta")
    print("7. Rosa")
    color = input("Elija el número: ")
    if color == "1":
        color = "ROJO"
        print("Su robot es ROJO")
        break
    elif color == "2":
        color = "NARANJA"
        print("Su robot es NARANJA")
        break
    elif color == "3":
        color = "AMARILLO"
        print("Su robot es AMARILLO")
        break
    elif color == "4":
        color = "VERDE"
        print("Su robot es VERDE")
        break
    elif color == "5":
        color = "AZUL"
        print("Su robot es AZUL")
        break
    elif color == "6":
        color = "VIOLETA"
        print("Su robot es VIOLETA")
        break
    elif color == "7":
        color = "ROSA"
        print("Su robot es ROSA")
        break
    else:
        print("INGRESE UN DATO VÁLIDO")
        input("Presione Enter")
while True:
    print("¿Qué tipo de robot desea?")
    print("  1. Carpintero")
    print("  2. Cocinero")
    print("  3. Limpieza")
    print("  4. Niñero")
    tipo = input("Elija el número: ")
    if tipo == "1":
        robot = Carpintero(nombre, color)
        print("Robot de tipo CARPINTERO")
        break
    if tipo == "2":
        robot = Cocinero(nombre, color)
        print("Robot de tipo COCINERO")
        break
    if tipo == "3":
        robot = RobotLimpieza(nombre, color)
        print("Robot de tipo LIMPIEZA")
        break
    if tipo == "4":
        robot = Niñero(nombre, color)
        print("Robot de tipo NIÑERO")
        break
    else:
        print("INGRESE UN DATO VÁLIDO")
        input("Presione Enter")
