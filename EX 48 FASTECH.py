x = int(input('Digite um número: '))
atual = 1
fatorial = 1
while atual <= x:
    fatorial *= atual
    atual += 1
    print(fatorial)
print('O Fatorial de: ', x, ' Vale: ', fatorial)
