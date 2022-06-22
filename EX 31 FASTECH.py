n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite um outro número: '))
while n1 == n2 or n2 == n3 or n3 == n1:
    n1 = float(input('Números repetidos, digite novamente o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    n3 = float(input('Digite o terceiro número: '))
maior = max(n1, n2, n3)
menor = min(n1, n2, n3)
if maior == n1 and menor == n2 or maior == n2 and menor == n1:
    print('A Ordem crescente dos números é: ', maior, n3, menor)
if maior == n2 and menor == n3 or maior == n3 and menor == n2:
    print('A Ordem crescente dos números é: ', maior, n1, menor)
if maior == n3 and menor == n1 or maior == n1 and menor == n3:
    print('A Ordem crescente dos números é: ', maior, n2, menor)