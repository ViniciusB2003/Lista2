x = bool(input('Digite True para verdadeiro ou False para falso: '))
print(x)
y = input('Digite True para verdadeiro ou False para falso: ')
print(y)
while x != True and x != False:
    x = input('Valor inválido, digite True para verdadeiro ou False para falso: ')
while y != True and y != False:
    y = input('Valor inválido, digite True para verdadeiro ou False para falso: ')
if x == True and y == True:
    print('Ambos são valores verdadeiros')
elif x == False and y == False:
    print('Ambos são valores falsos')
if x != y:
    print('Os valores digitados são distinstos')