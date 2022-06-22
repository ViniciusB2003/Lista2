Tolerancia = 500
C = 0
n = 1
S = 0
while C < Tolerancia:
    if n % 3 == 0:
        S = S + n
    n = n + 2
    C = C + 1
print('O Resultado da soma de ímpares entre 1 e 500 é: ', S)
