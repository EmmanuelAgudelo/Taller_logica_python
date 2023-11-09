def getA():
    while True:
        getA = input("Ingrese la variable de A (0 o 1): ")
        if getA in ('0', '1'):
            return int(getA)
        else:
            print("Variable no válida. Intente de nuevo.")

def getB():
    while True:
        getB = input("Ingrese la variable  de B (0 o 1): ")
        if getB in ('0', '1'):
            return int(getB)
        else:
            print("Variable no válidoa. Intente de nuevo.")