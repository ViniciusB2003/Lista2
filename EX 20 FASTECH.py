import math
X1 = float(input('Onde o primeiro ponto se encontra no eixo X: '))
Y1 = float(input('Onde o primeiro ponto se encontra no eixo y: '))
X2 = float(input('Onde o segundo ponto se encontra no eixo X: '))
Y2 = float(input('Onde o segundo ponto se encontra no eixo Y: '))
D = math.sqrt(((X2 - X1) * (X2 - X1)) + ((Y2 - Y1) * (Y2 - Y1)))
print('A Distância entre dois pontos vale: ', D)
