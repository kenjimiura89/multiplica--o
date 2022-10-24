from ctypes.wintypes import PINT


def area(a, b):
    print(f'A = {a} e B = {b}')
    s = a * b
    print(f'A área do terreno é {s} metros quadrados')

#Programa principal

a =  float(input('informe o valor de a '))
b =  float(input('informe valor de b '))
area(a, b)