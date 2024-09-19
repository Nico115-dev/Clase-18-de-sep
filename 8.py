def multiplicacion(numero: int):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")


if(__name__ == "__main__"):
    numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
    multiplicacion(numero)
