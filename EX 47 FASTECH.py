A = int(input('Digite o valor inicial: '))
razao = int(input('Digite o valor da razao: '))
S = 0.0
contador = 1
multiplicador = 1
while contador <= 10:
    S = A * (razao**multiplicador)
    multiplicador += 1
    contador += 1
    print(S)