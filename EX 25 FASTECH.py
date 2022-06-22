nome = str(input('Digite o seu nome: '))
sexo = str(input('Digite o seu sexo, sendo MASCULINO ou FEMININO: '))
while sexo != 'MASCULINO' and sexo != 'FEMININO':
    sexo = str(input('Sexo inválido, digite novamente:'))
Ec = str(input('Digite seu estado civíl, sendo CASADA(O) ou SOLTEIRA(O): '))
while Ec != 'CASADA' and Ec != 'CASADO' and Ec != 'SOLTEIRA' and Ec != 'SOLTEIRO':
    Ec = str(input('Estado Civíl inválido, digite novamente: '))
if sexo == 'FEMININO' and Ec == 'CASADA':
    T = int(input('Digite tempo de casada: '))
