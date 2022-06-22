Pn = float(input('Digite o preço da etiqueta do produto: '))
condicao = str(input('Digite a condição do pagamento, sendo: À VISTA EM DINHEIRO OU CHEQUE; À VISTA NO CARTÃO DE CRÉDITO; DUAS VEZES COM JUROS; DUAS VEZES SEM JUROS: '))
while condicao != 'À VISTA EM DINHEIRO OU CHEQUE' and condicao != 'À VISTA NO CARTÃO DE CRÉDITO' and condicao != 'DUAS VEZES COM JUROS' and condicao != 'DUAS VEZES SEM JUROS':
    condicao = str(input('Condicao inválida, digite novamente: '))
if condicao == 'À VISTA EM DINHEIRO OU CHEQUE':
    Pf = Pn - (Pn * 0.1)
    print('O Valor a ser pago é de R$', Pf)
if condicao == 'À VISTA NO CARTÃO DE CRÉDITO':
    Pf = Pn - (Pn * 0.15)
    print('O Valor a ser pago é de R$', Pf)
if condicao == 'DUAS VEZES COM JUROS':
    Pf = ((Pn * 0.1) + Pn)/2
    print('O Valor a ser pago é de 2 parcelas de R$', Pf, ' Com 10% de juros')
if condicao == 'DUAS VEZES SEM JUROS':
    Pf = Pn/2
    print('O Valor a ser pago é de 2 parcelas de R$', Pf)
