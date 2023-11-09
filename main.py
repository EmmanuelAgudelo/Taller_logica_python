import os
import time
from controller.setOption import setOption
from controller.getVariables import getA,getB


# Mensaje dinámico
os.system('cls') 
print("****************************************") 
print("*                                      *")
print("*   ¡Bienvenidos al taller de lógica   *")
print("*                                      *")
print("****************************************")
 
time.sleep(2)
os.system('cls')

while True:
    cnt = input('¿Deseas comenzar? y/n: ')
    if cnt == 'y':
        break
    elif cnt =='n':
        print('¡Gracias por usar nuestro programa!')
        exit()
    else:
        print('Escribe y o n (Yes or No)')

os.system('cls')
print("¡Excelente, comencemos¡")
time.sleep(1)
print("Loading...")
time.sleep(1)
os.system('cls')


A = getA()
B = getB()
print('Las variables son: \n'
        ' A = '+str(A)+'\n'
        ' B = '+str(B)+'\n')

while True:
    print('**************** MENÚ ****************\n\n'
        'Elije la opción que deseas realizar:\n\n'
          ' 1. Compuerta NOT para la variable A.\n'
          ' 2. Compuerta AND para las variables A y B.\n'
          ' 3. Compuerta OR para las variables A y B.\n'
          ' 4. Compuerta XOR para las variables A y B.\n'
          ' 5. Compuerta NAND para las variables A y B.\n'
          ' 6. Compuerta NOR para las variables A y B.\n'
          ' 7. Compuerta XNOR para las variables A y B.\n'
          ' 8. Compuerta IF para la variable A.\n'
          ' 9. Circuito lógico\n'
          ' 10. Dibujar compuerta NOT\n'
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





