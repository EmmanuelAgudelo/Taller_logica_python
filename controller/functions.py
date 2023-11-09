from turtle import *

def compuerta_AND(A,B):
    result = (A & B)
    print("\nResultado de la Compuerta AND para A y B es: ",result,'\n')
    print('--------------------------------------------------------------')

def compuerta_OR(A, B):
    result = 1 if (A | B) else 0
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

def compuerta_logica(A,B):
    result = 1 if not((((not (A)) | B) & (not B)) & (not B))else 0 | 1 if(not (A)) else 0 
    
    print('\nEl circuito lógico será: [((a`+b)*b`)*b`]`+a`\n')
    print('Reemplazamos las variables con los datos ingresados\n\n')
    print('   [((',A,'`+',B,')*',B,'`)*',B,'`]`+',A,'`\n\n')
    print('Soluciónes parciales: \n')
    print('= [(',((not A) | B),'*',B,'`)*',B,'`]`+',A,'`\n')
    print('= [(',((not A) | B),'*',1 if not(B) else 0,')*',1 if not(B) else 0,']`+',1 if not(A) else 0,'\n')
    print('= [(',((not A) | B) & (not B),')*',1 if not(B) else 0,']`+',1 if not(A) else 0,'\n')
    print('= [',((((not A) | B) & (not B)) & (not B)),']`+',1 if not(A) else 0,'\n')
    print('= ', 1 if not((((not A) | B) & (not B)) & (not B)) else 0,'+',1 if not(A) else 0,'\n')
    print('= ', 1 if not((((not A) | B) & (not B)) & (not B)) else 0 | 1 if (not(A)) else 0,'\n\n')
    print('TABLA DE VERDAD\n')
    print('| A | B | [((a` + b) *  b`) *  b`] ` +  a`\n'  
          '----------------------------------------- \n'
          '| 0 | 0 |    1  1    1  1   1  1  0 |1| 1 \n'
          '| 0 | 1 |    1  1    0  0   0  0  1 |1| 1 \n'
          '| 1 | 0 |    0  0    0  1   0  1  1 |1| 0 \n'
          '| 1 | 1 |    0  1    0  0   0  0  1 |1| 0 \n'
          '                                    |_|   \n'
          )

    print('--------------------------------------------------------------')

def compuerta_draw():
    setup(450, 200, 0, 0)
    screensize(200, 150)
    colormode(255)
    hideturtle()
    penup()
    left(180)
    forward(100)
    right(180)
    pendown()
    forward(100)
    right(90)
    forward(50)
    left(180)
    forward(100)
    right(120)
    forward(100)
    right(120)
    forward(100)
    right(180)
    forward(100)
    right(50)
    dot(10, 0, 0, 0)
    exitonclick()
    try:
        bye()
    except Terminator:
        pass
    print('--------------------------------------------------------------')