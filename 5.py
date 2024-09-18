def passw(password:str):
    if(len(password)>= 8 and any(char.isdigit() for char in password)):
        print("Contraseña Valida")
    else:
        print("Contraseña Invalida")



if(__name__ == "__main__"):
        passw(input("Ingrese su contraseña previamente establecida: "))