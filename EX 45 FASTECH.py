n = int(input('Digite um número de 1 a 10: '))
while n < 1 or n > 10:
    n = int(input('Valor inválido, digite um número de 1 a 10: '))
multiplicador = 0
while multiplicador <= 10:
    r = multiplicador * n
    print(multiplicador, ' x ', n, ' = ', r)
    multiplicador += 1