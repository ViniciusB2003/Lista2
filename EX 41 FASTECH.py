x = int(input('Digite um número: '))
I1 = 0
I2 = 0
I3 = 0
I4 = 0
while x > 0:
    if x >= 0 and x <= 25:
        I1 +=1
    if x >= 26 and x <= 50:
        I2 += 1
    if x >= 51 and x <= 75:
        I3 += 1
    if x >= 76 and x <= 100:
        I4 += 1
    x = int(input('Digite outro número, o cálculo para quando digitar um número negativo: '))
print('A Quantidade de números entre 0 e 25 é: ', I1)
print('A Quantidade de números entre 26 e 50 é: ', I2)
print('A Quantidade de números entre 51 e 75 é: ', I3)
print('A Quantidade de números entre 76 e 100 é: ', I4)
