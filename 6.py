from datetime import datetime

def fechaValida(fecha: str):
    try:
        variable = datetime.strptime(fecha, "%Y-%m-%d")
        año = variable.year
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            print(f"El año {año} es bisiesto.")
        else:
            print(f"El año {año} no es bisiesto.")
        
        return True
    except ValueError:
        return False

if(__name__ == "__main__"):

    fecha = input("Ingrese una fecha en el formato aaaa-mm-dd: ")
    if fechaValida(fecha):
        print(f"La fecha {fecha} es válida.")
    else:
        print(f"La fecha {fecha} no es válida.")


