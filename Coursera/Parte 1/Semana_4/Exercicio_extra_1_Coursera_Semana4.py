num = int (input("Digite um número inteiro: "))

i = 1
num_divisoes = 0

while i <= num:
    resultado = num % i
    i = i+1

    if (resultado == 0):
        num_divisoes = num_divisoes + 1

if (num_divisoes == 2):
    print ("primo")

else:
    print ("não primo")