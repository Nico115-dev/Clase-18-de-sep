def Triangulo(a: float, b: float, c: float):
    if (a + b > c and a + c > b and b + c > a):
        return True
    else:
        return False

if(__name__ == "__main__"):
    
    a = float(input("Ingresa la longitud del primer lado: "))
    b = float(input("Ingresa la longitud del segundo lado: "))
    c = float(input("Ingresa la longitud del tercer lado: "))
    
    if Triangulo(a, b, c):
        print("Las longitudes ingresadas pueden formar un triángulo válido.")
    else:
        print("Las longitudes ingresadas no pueden formar un triángulo válido.")


