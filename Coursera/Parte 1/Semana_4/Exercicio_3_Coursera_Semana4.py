num = int (input ("Digite um numero: "))

soma = 0

while num != 0:
  soma = soma + (num % 10)
  num = num // 10

print (soma)