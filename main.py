import os

n = 1
soma = 0 
cont = 0
while (n > 0):
  n = int(input("Digite um número:"))
  os.system('clear')
  if( n % 2 == 0 and n % 5 == 0 and n > 0 ):
    soma = soma + n
    cont = cont + 1
    media = soma / cont
else:
  print("A média dos números pares e multiplos de cinco é: ",media)
  
  