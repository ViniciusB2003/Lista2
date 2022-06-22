x = float(input('Digite um número, o cálculo para quando digitar 0: '))
positivo = 0
negativo = 0
contador = 0
soma = 0
while x != 0:
    if x > 0:
        positivo += 1
    if x < 0:
        negativo += 1
    soma = soma + x
    contador += 1
    x = float(input('Digite outro número, o cálculo para quando digitar 0: '))
media = soma/contador
percentualp = (100 * positivo)/contador
percentualn = (100 * negativo)/contador
print('A Média dos valores digitados é: ', media)
print('A Quantidade de valores positivos e negativos respectivamente é: ', positivo, ' e ', negativo)
print('A Porcentagem de valores positivos e negativos respectivamente é: ', percentualp,'%', ' e ', percentualn, '%')
