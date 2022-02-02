#calcular combinações de N termos k a k. coeficiente binomial

def fatorar (x):
    fatoracao = 1
    i = 2
    while i <= n:
        fatoracao = fatoracao * i
        i = i+1
    return fatoracao

n = int (input ("Digite o valor de n: "))
k = int (input ("Digite o valor de k: "))

a = fatorar (n)
b = fatorar (k)
c = fatorar (n-k)

numero_binomial = a / b * c

print (numero_binomial)