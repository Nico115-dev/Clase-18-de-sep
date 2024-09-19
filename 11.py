def calcularValorPagar(mesConsumo: str, valorKw: float, totalKwConsumido: float, estrato: int):

    if estrato == 1:
        tarifaEstrato = 1.0
    elif estrato == 2:
        tarifaEstrato = 1.2
    elif estrato == 3:
        tarifaEstrato = 1.5
    elif estrato == 4:
        tarifaEstrato = 1.8
    elif estrato == 5:
        tarifaEstrato = 2.0
    else:
        tarifaEstrato = 1.0  

    valorTotal = totalKwConsumido * valorKw * tarifaEstrato
    return valorTotal

def ingresarDatos():
    mesConsumo = input("Ingrese el mes de consumo: ")
    valorKw = float(input("Ingrese el valor por kilovatio (kW): "))
    totalKwConsumido = float(input("Ingrese el total de kilovatios consumidos en el mes: "))
    estrato = int(input("Ingrese el estrato del usuario (1-5): "))

    valorPagar = calcularValorPagar(mesConsumo, valorKw, totalKwConsumido, estrato)

    print(f"\nResumen de consumo para el mes de {mesConsumo}:")
    print(f"Valor por kW: {valorKw:}")
    print(f"Total kW consumidos: {totalKwConsumido:}")
    print(f"Estrato: {estrato}")
    print(f"Valor a pagar: {valorPagar:}")

ingresarDatos()
