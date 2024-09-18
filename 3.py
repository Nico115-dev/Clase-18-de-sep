def pais(name:str): 
    name = name.upper()
    if (name == "CHILE" or name == "BRASIL"):
        print("Su pais pertenece a America")
    elif (name == "CHINA" or name == "JAPON"):
        print("Su pais pertenece a Asia")
    elif (name == "ESPAÑA" or name == "PORTUGAL"):
        print("Su pais pertenece a Europa")
    elif (name == "AUSTRALIA" or name == "CAMBOYA"):
        print("Su pais pertenece a Oceania")
    else:
        print("El pais no esta dentro de los paises registrados")


 
pais(input("Ingrese su pais : "))