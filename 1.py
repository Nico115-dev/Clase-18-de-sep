def edad():
    edad = int(input("Ingrese su edad: "))
    if edad >= 18:
        print("Eres mayor de edad ")
    elif edad < 18:
        print("Eres menor de edad ")
    
edad()