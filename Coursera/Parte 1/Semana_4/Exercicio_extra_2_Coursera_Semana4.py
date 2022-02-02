num = int (input ("Digite um número inteiro: "))

iguais = False

while num > 0:
  comparacao = num % 10
  num2 = num // 10
  comparacao2 = num2 % 10
  num = num2

  if comparacao == comparacao2:
    print ("sim")
    iguais = True

if not iguais:
    print ("não")