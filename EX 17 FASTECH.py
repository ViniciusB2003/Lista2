FCusto = float(input('Digite o custo de fábrica do carro novo: '))
PDistribuidor = 0.28
PImpostos = 0.45
Vf = (FCusto * PDistribuidor + FCusto) + (FCusto * PImpostos + FCusto)
print('O Custo ao consumidor será de R$', Vf)
