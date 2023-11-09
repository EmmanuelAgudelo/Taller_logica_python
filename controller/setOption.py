from controller import functions

def setOption(option, A, B):
    if(option == '1'):
        functions.compuerta_NOT(A)
    elif(option == '2'):
        functions.compuerta_AND(A,B),
    elif(option == '3'):
        functions.compuerta_OR(A,B),
    elif(option == '4'):
        functions.compuerta_XOR(A,B),
    elif(option == '5'):
        functions.compuerta_NAND(A,B),
    elif(option == '6'):
        functions.compuerta_NOR(A,B),
    elif(option == '7'):
        functions.compuerta_XNOR(A,B),
    elif(option == '8'):
        functions.compuerta_IF(A),
    elif(option == '9'):
        functions.compuerta_logica(A,B)
    elif(option == '10'):
        functions.compuerta_draw()