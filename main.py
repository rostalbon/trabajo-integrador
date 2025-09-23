from cocinero import Cocinero

titulo_programa = "ROBOT"
print(f"╔═{"═" * len(titulo_programa)}═╗")
print(f"║ {" " * len(titulo_programa)} ║")
print(f"║ {titulo_programa} ║")
print(f"║ {" " * len(titulo_programa)} ║")
print(f"╚═{"═" * len(titulo_programa)}═╝")

print("~ DATOS DEL ROBOT ~")
nombre = input("Asígnele un nombre a su robot: ")
color = input("Ingrese le color de su robot: ")
while True:
    print("¿Qué tipo de robot desea?")
    print("  1. Carpintero")
    print("  2. Cocinero")
    print("  3. Limpieza")
    print("  4. Niñero")
    tipo = input("Elija el número que desea: ")
    if tipo == "2":
        robot = Cocinero(nombre, color)
        print(robot.batir())