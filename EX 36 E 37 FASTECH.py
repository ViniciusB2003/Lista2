ni = int(input('Digite o número de identificação do aluno: '))
n1 = float(input('Digite a 1° Nota: '))
n2 = float(input('Digite a 2° Nota: '))
n3 = float(input('Digite a 3° Nota: '))
Mex = float(input('Digite a média da nota dos exercícios: '))
MA = (n1 + n2 * 2 + n3 * 3 + Mex)/7
print('A Média de aproveitamento do aluno: ', ni, 'É de: ', MA)
if MA >= 90:
    conceito = 'A'
if MA >= 75 and MA < 90:
    conceito = 'B'
if MA >= 60 and MA < 75:
    conceito = 'C'
if MA >= 40 and MA < 60:
    conceito = 'D'
if MA < 40:
    conceito = 'E'
if conceito == 'A' or conceito == 'B' or conceito == 'C':
    print('O Aluno: ', ni, 'tem como notas de verificação: ', n1, n2, n3)
    print('A Média dos exercícios: ', Mex, 'Média de Aproveitamento: ', MA)
    print('Alcancou o conceito: ', conceito, 'Sendo considerado APROVADO')
elif conceito == 'D' or conceito == 'E':
    print('O Aluno: ', ni, 'tem como notas de verificação: ', n1, n2, n3)
    print('A Média dos exercícios: ', Mex, 'Média de Aproveitamento: ', MA)
    print('Alcancou o conceito: ', conceito, 'Sendo considerado REPROVADO')
