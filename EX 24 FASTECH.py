A = int(input('Digite um número: '))
B = int(input('Digite outro número: '))
C = int(input('Digite outro número: '))
S = A + B
if S < C:
    print('A Soma de A + B, que vale: ', S, ' É menor que: ', C)
if S == C:
    print('A Soma de A + B, que vale: ', S, ' É igual a: ', C)
if S > C:
    print('A Soma de A + B, que vale: ', S, ' É maior que: ', C)