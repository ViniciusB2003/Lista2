x1 = float(input('Digite a 1° altura: '))
x2 = float(input('Digite a altura seguinte: '))
maior = max(x1, x2)
menor = min(x1, x2)
contador = 2
while contador < 15:
    x1 = float(input('Digite a próxima altura: '))
    if x1 > maior:
        maior = x1
    elif x1 < menor:
        menor = x1
    contador += 1
print('A Menor altura é: ', menor, ' E a maior altura é: ', maior)