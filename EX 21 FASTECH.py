Salario = float(input('Digite, em reais, o salário bruto do funcionário: '))
Impostos = 0.08
Saumentado = Salario + (Salario * 0.15)
Sfinal = Saumentado - (Saumentado * Impostos)
print('O Salário com aumento  é de R$', Saumentado)
print('O Salário Liquido do funcionário é de R$', Sfinal)
