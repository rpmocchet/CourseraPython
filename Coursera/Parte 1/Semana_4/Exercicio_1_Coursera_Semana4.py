n = int (input ("Digite o valor de n: "))

#fatoracao = n * (n-1)
fatoracao = 1
i = 2

while i <= n:
  fatoracao = fatoracao * i
  i = i+1

print (fatoracao)