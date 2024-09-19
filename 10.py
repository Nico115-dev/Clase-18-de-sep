from datetime import datetime

def calcularAntiguedadEmpleado(añoIngreso: int):
    añoActual = datetime.now().year
    return añoActual - añoIngreso

def ingresarInfoEmpleado():
    nombre = input("Ingrese el nombre del empleado: ")
    apellidos = input("Ingrese los apellidos del empleado: ")
    telefono = input("Ingrese el teléfono del empleado: ")
    añoIngreso = int(input("Ingrese el año de ingreso a la empresa: "))
    edad = int(input("Ingrese la edad del empleado: "))

    antiguedad = calcularAntiguedadEmpleado(añoIngreso)

    print("\nInformación del empleado:")
    print(f"Nombre: {nombre}")
    print(f"Apellidos: {apellidos}")
    print(f"Antigüedad: {antiguedad} años")

if(__name__ == "__main__"):
    ingresarInfoEmpleado()