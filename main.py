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
nombre = input("Asígnele un nombre a su robot: ").upper()
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
while True:
    print(f"╔═{"═" * len(titulo_programa)}═╗")
    print(f"║ {" " * len(titulo_programa)} ║")
    print(f"║ {titulo_programa} ║")
    print(f"║ {" " * len(titulo_programa)} ║")
    print(f"╚═{"═" * len(titulo_programa)}═╝")
    print("1. Ver características")
    print("2. ¿Qué tarea está realizando ahora?")
    print("3. Elegir una tarea para que realice")
    print("4. Salir")
    res = input("Elija un número: ")
    if res == "1":
        print(f"Nombre: {robot.get_nombre()}")
        print(f"Color: {robot.get_color()}")
        if tipo == "1":
            print("Tipo: CARPINTERO")
        elif tipo == "2":
            print("Tipo: COCINERO")
        elif tipo == "3":
            print("Tipo: LIMPIEZA")
        else:
            print("Tipo: NIÑERO")
    elif res == "2":
        print(robot.get_trabajo())
        input("Presione enter para salir al menú")
    elif res == "3":
        while True:
            print(f"Estado actual: {robot.get_trabajo()}")
            print("1. Salir al menú principal")
            if tipo == "1":
                print("2. Hachar / Dejar de hachar")
                print("3. Cerruchar / Dejar de cerruchar")
                print("4. Atornillar / Dejar de atornillar")
                resTrabajo = input("Elija un número: ")
                if resTrabajo == "1":
                    break
                elif resTrabajo == "2":
                    print(robot.hachar())
                elif resTrabajo == "3":
                    print(robot.cerruchar())
                elif resTrabajo == "4":
                    print(robot.atornillar())
                else:
                    print("Ingrese un dato válido")
            elif tipo == "2":
                print("2. Batir / Dejar de batir")
                print("3. Revolver / Dejar de revolver")
                print("4. Cortar / Dejar de cortar")
                resTrabajo = input("Elija un número: ")
                if resTrabajo == "1":
                    break
                elif resTrabajo == "2":
                    print(robot.batir())
                elif resTrabajo == "3":
                    print(robot.revolver())
                elif resTrabajo == "4":
                    print(robot.cortar())
                else:
                    print("Ingrese un dato válido")
            elif tipo == "3":
                print("2. Barrer / Dejar de barrer")
                print("3. Aspirar / Dejar de aspirar")
                print("4. Trapear / Dejar de trapear")
                resTrabajo = input("Elija un número: ")
                if resTrabajo == "1":
                    break
                elif resTrabajo == "2":
                    print(robot.barrer())
                elif resTrabajo == "3":
                    print(robot.aspirar())
                elif resTrabajo == "4":
                    print(robot.trapear())
                else:
                    print("Ingrese un dato válido")
            else:
                print("2. Limpiar / Dejar de limpiar")
                print("3. Dar mamadera / Dejar de dar mamadera")
                print("4. Arropar / Dejar de arropar")
                resTrabajo = input("Elija un número: ")
                if resTrabajo == "1":
                    break
                elif resTrabajo == "2":
                    print(robot.limpiar())
                elif resTrabajo == "3":
                    print(robot.darMamadera())
                elif resTrabajo == "4":
                    print(robot.arropar())
                else:
                    print("Ingrese un dato válido")
