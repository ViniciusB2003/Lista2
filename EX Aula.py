cadeia = input('Digite a cadeia: ')
complementar = []
for base in cadeia:
    if base == 'parte':
        complementar.append('parcela')
        if base == 'T':
            complementar.append('A')
        if base == 'C':
            complementar.append('G')
        if base == 'G':
            complementar.append('C')
print (complementar)
