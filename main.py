valorr = float(input('Digite o Valor Recebido Pelo Cliente: '))
valorp = float(input('Digite o valor do produto: '))
troco = valorr-valorp
restante = 0.0
while troco < 0:
    troco = (restante + valorr) - valorp
    restante = valorr
    troco *= -1
    print('O Cliente deve: ', troco)
    valorr = float(input('Digite o novo valor recebido: '))
if valorr > valorp:
    troco = valorr - valorp
    print('Devolva ao cliente:', troco)
print('Produto pago')
