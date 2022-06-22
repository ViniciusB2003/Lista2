massa = float(input('Digite sua massa corporal, em Quilos: '))
altura = float(input('Digite sua altura, em metros: '))
IMC = massa/(altura**2)
if IMC < 18.5:
    print('Seu IMC de: ', IMC, 'O Classifica como Abaixo do Peso')
if IMC > 18 and IMC < 25:
    print('Seu IMC de: ', IMC, 'O Classifica como Peso Normal')
if IMC >= 25 and IMC <= 30:
    print('Seu IMC de: ', IMC, 'O Classifica como Acima do Peso')
if IMC > 30:
    print('Seu IMC de: ', IMC, 'O Classifica como Obeso')

