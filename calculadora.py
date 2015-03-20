import cmath
import math
import os

def raiz(x):
    if((type(x) is complex) or (x<0)):
        return cmath.sqrt(x)
    else:
        return math.sqrt(x)

def multiplica(x,y):
    return x*y

def divide(x,y):
    if(y==0):
        return "\nErro: Nao e possivel dividir por zero"
    else:
        return x/y

def soma(x,y):
    return x+y

def subtrai(x,y):
    return x-y

def digitaX():
    if(input("O proximo numero a ser digitado e complexo (S ou N):  ").lower() == 's'):
        return complex(input("Digite o valor de x: "))
    else:
        return float(input("Digite o valor de x: "))

def digitaY():
    if(input("O proximo numero a ser digitado e complexo (S ou N):  ").lower() == 's'):
        return complex(input("Digite o valor de y: "))
    else:
        return float(input("Digite o valor de y: "))

def menu():
    print("""Qual operacao deseja fazer:
        1: Soma
        2: Subtracao
        3: Multiplicacao
        4: Divisao
        5: Raiz Quadrada
        0: Sair""")
    return int(input("\nOpcao: "))

opcao = menu()
while(opcao != 0):
    if(opcao == 1):
        x = digitaX()
        y = digitaY()        
        print("\n{0:4.2f} + {1:4.2f} = {2:4.2f}".format(x,y,soma(x,y)))
    elif(opcao == 2):
        x = digitaX()
        y = digitaY()
        print("\n{0:4.2f} - {1:4.2f} = {2:4.2f}".format(x,y,subtrai(x,y)))
    elif(opcao == 3):
        x = digitaX()
        y = digitaY()
        print("\n{0:4.2f} * {1:4.2f} = {2:4.2f}".format(x,y,multiplica(x,y)))
    elif(opcao == 4):
        x = digitaX()
        y = digitaY()
        if(y == 0):
            print(divide(x,y))
        else:
            print("\n{0:4.2f} / {1:4.2f} = {2:4.2f}".format(x,y,divide(x,y)))
    elif(opcao == 5):
        x = digitaX()
        print("\nA raiz quadrada de {0:4.2f} = {1:4.2f}".format(x,raiz(x)))
    input("\nDigite qualquer tecla para continuar.")
    os.system('cls')
    opcao = menu()

