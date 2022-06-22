numero = int(input('Digite um número de até 3 dígitos: '))
while numero > 999:
    numero = int(input('Valor inválido, digite um número de até 3 dígitos: '))
centena = numero//100
unidade = numero%100
unidade = unidade%10
dezena = numero//10
dezena = dezena%10
print('A Centena do número digitado é: ', centena, 'A Dezena é: ', dezena, ' E a unidade é: ', unidade)
