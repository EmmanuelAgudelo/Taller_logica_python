import os

# ------------- SOLICITAR VARIABLES -------------
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


#---------- FUNCIONES --------------

def compuerta_AND(A,B):
    result = (A & B)
    print("Resultado de la Compuerta AND para A y B es: ",result)

def compuerta_OR(A, B):
    result = (A | B)
    print("Resultado de la Compuerta OR para A y B es: ",result)

def compuerta_XOR(A, B):
    result = (A ^ B)
    print("Resultado de la Compuerta XOR para A y B es: ",result)

def compuerta_NOT(A):
    result = 1 if A == 0 else 0
    print("Resultado de la Compuerta NOT para A es: ", result)


def compuerta_NOR(A, B):
    result = 1 if not (A | B) else 0
    print("Resultado de la Compuerta NOR para A y B es: ", result)

def compuerta_XNOR(A, B):
    result = 1 if A == B else 0
    print("Resultado de la Compuerta XNOR para A y B es: ", result)

def compuerta_NAND(A,B):
    result = not(A & B)
    print("Resultado de la Compuerta NAND para A y B es: ",result)

def compuerta_IF(A):
    print("Resultado de la Compuerta IF para A es: ",A)


# ---------- SIMULADORE DE SWITCH --------------

def setOption(option, A, B):
    return {
        '1': compuerta_NOT(A),
        '2': compuerta_AND(A,B),
        '3': compuerta_OR(A,B),
        '4': compuerta_XOR(A,B),
        '5': compuerta_NAND(A,B),
        '6': compuerta_NOR(A,B),
        '7': compuerta_XNOR(A,B),
        '8': compuerta_IF(A),
    }.get(option)

# ----------- MENÚ ------------------------

print('***********TALLER #3 LÓGICA MATEMÁTICA************\n')
A = getA()
B = getB()

while True:
    print('\nLas variables son: \n'
          ' A = '+str(A)+'\n'
          ' B = '+str(B)+'\n')

    print('Menú:\n'
          ' 1. Compuerta NOT para la variable A.\n'
          ' 2. Compuerta AND para las variables A y B.\n'
          ' 3. Compuerta OR para las variables A y B.\n'
          ' 4. Compuerta XOR para las variables A y B.\n'
          ' 5. Compuerta NAND para las variables A y B.\n'
          ' 6. Compuerta NOR para las variables A y B.\n'
          ' 7. Compuerta XNOR para las variables A y B.\n'
          ' 8. Compuerta IF para la variable A.\n'
          ' 9. Circuito lógico\n'
          ' 10. Dibujar compuerta (indicar cual en esta opción)\n'
          ' 11. Cambiar variables.\n'
          ' 12. Limpiar pantalla.\n'
          ' 13. Salir.\n')
    option = input('Ingrese la opción del menú que desea ver: ')

    if (option == '13'):
        break
    elif (option =='12'):
        os.system("cls")
    elif (option == '11'):
        A = getA()
        B = getB()
    else:
        setOption(option, A, B)

