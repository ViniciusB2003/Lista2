numero = float(input('Digite um número: '))
if numero >= 0:
    Op = numero * 2
    print('O Dobro desse número vale: ', Op)
elif numero < 0:
    Op = numero * 3
    print('O Triplo desse número vale: ', Op)