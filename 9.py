def promedio():
    suma = 0
    conteo = 0
    
    while True:
        try:
            number = float(input("Ingresa un número positivo (o un número negativo para terminar): "))
            
            if number < 0:
                break
            else:
                suma += number
                conteo += 1
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    if conteo > 0:
        promedio = suma / conteo
        print(f"El promedio de los números ingresados es: {promedio:}")
    else:
        print("No se ingresaron números positivos.")

if(__name__ == "__main__"):
    promedio()