x = int(input('Digite um número, o cálculo irá parar quando digitar 0: '))
somag = 0.0
somap = 0.0
mediag = 0.0
mediap = 0.0
contador = 0.0
par = 0
impar = 0

while x != 0:
    if x % 2 == 0:
        par += 1
        somap = somap + x
    else:
        impar += 1
        somag = somag + x
    contador += 1
    x = int(input('Digite outro número, o cálculo para quando digitar 0: '))
mediap = somap/par
mediag = (somap + somag)/contador
print('A Quantidade de números pares e ímpares, respectivamente é: ', par, ' E ', impar)
print('A Média dos números pares é: ', mediap, ' E a média geral é: ', mediag)