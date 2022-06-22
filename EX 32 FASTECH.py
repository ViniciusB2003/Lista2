sexo = str(input('Digite seu sexo, sendo F para feminino ou M para masculino: '))
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Sexo inválido, digite F para feminino ou M para masculino: '))
altura = float(input('Digite sua altura: '))
if sexo == 'M':
    Pi = (72.7 * altura) - 58
    print('O Seu peso ideal é de: ', Pi, 'Kg')
elif sexo == 'F':
    Pi = (62.1 * altura) - 44.7
    print('O Seu peso ideal é de: ', Pi, 'Kg')
