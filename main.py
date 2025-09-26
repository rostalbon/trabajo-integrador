from cocinero import Cocinero
from carpintero import Carpintero
from niñero import Niñero
from deLimpieza import RobotLimpieza
from accesorios import Accesorios

titulo_programa = "ROBOT"
print(f"╔═{"═" * len(titulo_programa)}═╗")
print(f"║ {" " * len(titulo_programa)} ║")
print(f"║ {titulo_programa} ║")
print(f"║ {" " * len(titulo_programa)} ║")
print(f"╚═{"═" * len(titulo_programa)}═╝")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~ DATOS DEL ROBOT ~")
nombre = input("Asígnele un nombre a su robot: ").upper()
print("=====================================================================================")
print(f"El nombre {nombre} fue asignado exitosamente")
print("=====================================================================================")
input("Presione Enter para continuar")
while True:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
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
        print("=====================================================================================")
        print("Su robot es ROJO")
        print("=====================================================================================")
        input("Presione Enter para continuar")
        break
    elif color == "2":
        color = "NARANJA"
        print("=====================================================================================")
        print("Su robot es NARANJA")
        print("=====================================================================================")
        input("Presione Enter para continuar")
        break
    elif color == "3":
        color = "AMARILLO"
        print("=====================================================================================")
        print("Su robot es AMARILLO")
        print("=====================================================================================")
        input("Presione Enter para continuar")
        break
    elif color == "4":
        color = "VERDE"
        print("=====================================================================================")
        print("Su robot es VERDE")
        print("=====================================================================================")
        input("Presione Enter para continuar")
        break
    elif color == "5":
        color = "AZUL"
        print("=====================================================================================")
        print("Su robot es AZUL")
        print("=====================================================================================")
        input("Presione Enter para continuar")
        break
    elif color == "6":
        color = "VIOLETA"
        print("=====================================================================================")
        print("Su robot es VIOLETA")
        print("=====================================================================================")
        input("Presione Enter para continuar")
        break
    elif color == "7":
        color = "ROSA"
        print("=====================================================================================")
        print("Su robot es ROSA")
        print("=====================================================================================")
        input("Presione Enter para continuar")
        break
    else:
        print("=====================================================================================")
        print("INGRESE UN DATO VÁLIDO")
        print("=====================================================================================")
        input("Presione Enter para volver")
while True:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("¿Qué tipo de robot desea?")
    print("  1. Carpintero")
    print("  2. Cocinero")
    print("  3. Limpieza")
    print("  4. Niñero")
    tipo = input("Elija el número: ")
    if tipo == "1":
        robot = Carpintero(nombre, color)
        print("=====================================================================================")
        print("Robot de tipo CARPINTERO")
        print("=====================================================================================")
        print("Presione Enter para continuar")
        break
    if tipo == "2":
        robot = Cocinero(nombre, color)
        print("=====================================================================================")
        print("Robot de tipo COCINERO")
        print("=====================================================================================")
        print("Presione Enter para continuar")
        break
    if tipo == "3":
        robot = RobotLimpieza(nombre, color)
        print("=====================================================================================")
        print("Robot de tipo LIMPIEZA")
        print("=====================================================================================")
        print("Presione Enter para continuar")
        break
    if tipo == "4":
        robot = Niñero(nombre, color)
        print("=====================================================================================")
        print("Robot de tipo NIÑERO")
        print("=====================================================================================")
        print("Presione Enter para continuar")
        break
    else:
        print("=====================================================================================")
        print("INGRESE UN DATO VÁLIDO")
        print("=====================================================================================")
        input("Presione Enter para volver")
while True:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"╔═{"═" * len(titulo_programa)}═╗")
    print(f"║ {" " * len(titulo_programa)} ║")
    print(f"║ {titulo_programa} ║")
    print(f"║ {" " * len(titulo_programa)} ║")
    print(f"╚═{"═" * len(titulo_programa)}═╝")
    print("~ MENÚ PRINCIPAL ~")
    print("1. Ver características")
    print("2. ¿Qué tarea está realizando ahora?")
    print("3. Elegir una tarea para que realice")
    print("4. Configuración de la batería")
    print("5. Modificar accesorios")
    print("6. Salir")
    res = input("Elija un número: ")
    if res == "1":
        print("=====================================================================================")
        print(f"Nombre: {robot.get_nombre()}")
        print(f"Color: {robot.get_color()}")
        print(f"Batería: {robot.get_bateria()}")
        print(f"Accesorios: {robot.get_accesorios()}")
        if tipo == "1":
            print("Tipo: CARPINTERO")
        elif tipo == "2":
            print("Tipo: COCINERO")
        elif tipo == "3":
            print("Tipo: LIMPIEZA")
        else:
            print("Tipo: NIÑERO")
        print("=====================================================================================")
        print("Presione Enter para volver al MENÚ PRINCIPAL")
    elif res == "2":
        print("=====================================================================================")
        print(robot.get_trabajo())
        print("=====================================================================================")
        input("Presione enter para salir al MENÚ PRINCIPAL")
    elif res == "3":
        while True:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
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
                    print("=====================================================================================")
                    print(robot.hachar())
                elif resTrabajo == "3":
                    print("=====================================================================================")
                    print(robot.cerruchar())
                elif resTrabajo == "4":
                    print("=====================================================================================")
                    print(robot.atornillar())
                else:
                    print("=====================================================================================")
                    print("Ingrese un dato válido")
                print("=====================================================================================")
            elif tipo == "2":
                print("2. Batir / Dejar de batir")
                print("3. Revolver / Dejar de revolver")
                print("4. Cortar / Dejar de cortar")
                resTrabajo = input("Elija un número: ")
                if resTrabajo == "1":
                    break
                elif resTrabajo == "2":
                    print("=====================================================================================")
                    print(robot.batir())
                elif resTrabajo == "3":
                    print("=====================================================================================")
                    print(robot.revolver())
                elif resTrabajo == "4":
                    print("=====================================================================================")
                    print(robot.cortar())
                else:
                    print("=====================================================================================")
                    print("Ingrese un dato válido")
                print("=====================================================================================")
            elif tipo == "3":
                print("2. Barrer / Dejar de barrer")
                print("3. Aspirar / Dejar de aspirar")
                print("4. Trapear / Dejar de trapear")
                resTrabajo = input("Elija un número: ")
                if resTrabajo == "1":
                    break
                elif resTrabajo == "2":
                    print("=====================================================================================")
                    print(robot.barrer())
                elif resTrabajo == "3":
                    print("=====================================================================================")
                    print(robot.aspirar())
                elif resTrabajo == "4":
                    print("=====================================================================================")
                    print(robot.trapear())
                else:
                    print("=====================================================================================")
                    print("Ingrese un dato válido")
                print("=====================================================================================")
            else:
                print("2. Limpiar / Dejar de limpiar")
                print("3. Dar mamadera / Dejar de dar mamadera")
                print("4. Arropar / Dejar de arropar")
                resTrabajo = input("Elija un número: ")
                if resTrabajo == "1":
                    break
                elif resTrabajo == "2":
                    print("=====================================================================================")
                    print(robot.limpiar())
                elif resTrabajo == "3":
                    print("=====================================================================================")
                    print(robot.darMamadera())
                elif resTrabajo == "4":
                    print("=====================================================================================")
                    print(robot.arropar())
                else:
                    print("=====================================================================================")
                    print("Ingrese un dato válido")
                print("=====================================================================================")
    elif res == "4":
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        bateria = input("Ingrese el porcentaje de batería (solo número): ")
        print("=====================================================================================")
        print(robot.set_bateria(bateria))
        print("=====================================================================================")
        input("Presione Enter para volver al MENÚ PRINCIPAL")
    elif res == "5":
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1. Añadir accesorio")
        print("2. Eliminar accesorio")
        print("3. Salir")
        resAccesorio = input("Elija un número: ")
        if resAccesorio == "1":
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            accesorio = input("Ingrese el nombre del accesorio: ").upper()
            accesorio_agregado = Accesorios(accesorio)
            print("=====================================================================================")
            print(robot.agregar_accesorio(accesorio))
            print("=====================================================================================")
        elif resAccesorio == "2":
            accesorios = robot.get_accesorios_array()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            if accesorios == []:
                print("=====================================================================================")
                print("Sin accesorios")
                print("=====================================================================================")
            else:
                for i in range (1, len(accesorios)+1, 1):
                    print(f"{i}. {accesorios[i-1]}")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                resEliminar = int(input("Elija el número que desea eliminar: "))
                print("=====================================================================================")
                print(robot.eliminar_accesorio(resEliminar))
                print("=====================================================================================")
            print("Presione Enter para volver al MENÚ PRINCIPAL")
    elif res == "6":
        break
    else:
        print("=====================================================================================")
        print("Ingrese un dato válido")
        print("=====================================================================================")
        input("Presione Enter para volver al MENÚ PRINCIPAL")