A = int(input('Digite o valor inicial: '))
razao = int(input('Digite o valor da razão: '))
contador = 1
multiplicador = 1
S = 0
while contador <= 10:
    S = A + (razao * multiplicador)
    multiplicador += 1
    contador += 1
    print(S)