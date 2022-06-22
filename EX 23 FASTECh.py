umcent = int(input('Há quantas moedas de 1 centavo no cofre: '))
cincocent = int(input('Há quantas moedas de 5 centavos no cofre: '))
dezcent = int(input('Há quantas moedas de 10 centavos no cofre: '))
vintecincocent = int(input('Há quantas moedas de 25 centavos no cofre: '))
cinquentacent = int(input('Há quantas moedas de 50 centavos no cofre: '))
umreal = int(input('Há quantas moedas de 1 real no cofre: '))

umcent = umcent/100
cincocent = (cincocent * 5)/100
dezcent = (dezcent * 10)/100
vintecincocent = (vintecincocent * 25)/100
cinquentacent = (cinquentacent * 50)/100
Vf = umcent + cincocent + dezcent + vintecincocent + cinquentacent + umreal
print('O Valor economizado no cofre é de R$', Vf)
