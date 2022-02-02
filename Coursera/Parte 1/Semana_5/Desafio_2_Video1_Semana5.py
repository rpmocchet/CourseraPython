#reorganizar o codigo de bhaskara em pequenas funcoes
import math

def delta(a,b,c):
    return (b ** 2 - 4 * a * c)

def main():
    a = float (input ("Digite um valor para a: "))
    b = float (input ("Digite um valor para b: "))
    c = float (input ("Digite um valor para c: "))
    calcula_raizes(a,b,c)

def calcula_raizes(a,b,c):
    d = delta (a,b,c)

    if d < 0:
        print ("A equação nao tem raízes reais.")
    else:
        raiz1 = -b + (math.sqrt(d)) / 2*a
        raiz2 = -b - (math.sqrt(d)) / 2*a

        print ("As raízes da equação são:",raiz1,"e",raiz2)
