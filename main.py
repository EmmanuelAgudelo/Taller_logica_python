import os
import time 

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
    print("\nResultado de la Compuerta AND para A y B es: ",result,'\n')
    print('--------------------------------------------------------------')

def compuerta_OR(A, B):
    result = (A | B)
    print("\nResultado de la Compuerta OR para A y B es: ",result,'\n')
    print('--------------------------------------------------------------')

def compuerta_XOR(A, B):
    result = (A ^ B)
    print("\nResultado de la Compuerta XOR para A y B es: ",result,'\n')
    print('--------------------------------------------------------------')

def compuerta_NOT(A):
    result = 1 if A == 0 else 0
    print("\nResultado de la Compuerta NOT para A es: ",result,'\n')
    print('--------------------------------------------------------------')


def compuerta_NOR(A, B):
    result = 1 if not (A | B) else 0
    print("\nResultado de la Compuerta NOR para A y B es: ",result,'\n')
    print('--------------------------------------------------------------')

def compuerta_XNOR(A, B):
    result = 1 if A == B else 0
    print("\nResultado de la Compuerta XNOR para A y B es: ",result,'\n')
    print('--------------------------------------------------------------')

def compuerta_NAND(A,B):
    result = not(A & B)
    print("\nResultado de la Compuerta NAND para A y B es: ",result,'\n')
    print('--------------------------------------------------------------')

def compuerta_IF(A):
    print("\nResultado de la Compuerta IF para A es: ",A,'\n')
    print('--------------------------------------------------------------')


# ---------- SIMULADORE DE SWITCH --------------

def setOption(option, A, B):
    if(option == '1'):
        compuerta_NOT(A)
    elif(option == '2'):
        compuerta_AND(A,B),
    elif(option == '3'):
        compuerta_OR(A,B),
    elif(option == '4'):
        compuerta_XOR(A,B),
    elif(option == '5'):
        compuerta_NAND(A,B),
    elif(option == '6'):
        compuerta_NOR(A,B),
    elif(option == '7'):
        compuerta_XNOR(A,B),
    elif(option == '8'):
        compuerta_IF(A),

# Mensaje dinámico
os.system('cls') 
print("****************************************") 
print("*                                      *")
print("*   ¡Bienvenidos al taller de lógica   *")
print("*                                      *")
print("****************************************")
 
time.sleep(2)
os.system('cls')

# ----------- MENÚ ------------------------
A = getA()
B = getB()
print('Las variables son: \n'
        ' A = '+str(A)+'\n'
        ' B = '+str(B)+'\n')

while True:
    print('**************** MENÚ ****************\n\n'
        'Elije la opción que deseas realizar:\n'
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
          ' 12. Salir.\n')

    option = input('Ingrese la opción del menú que desea ver: ')
    if (option == '12'):
        print('¡Gracias por usar nuestro programa!')
        break
    elif (option == '11'):
        os.system('cls')
        A = getA()
        B = getB()
        print('Las variables son: \n'
          ' A = '+str(A)+'\n'
          ' B = '+str(B)+'\n')
    else:
        setOption(option, A, B)
        time.sleep(2)



