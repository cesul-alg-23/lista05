ano = int(input('Informe o ano: '))

if (ano % 4 == 0) and ((ano % 400 == 0) or (ano % 100 != 0)):
    print(f'{ano} é bissexto!')
else:
    print(f'{ano} não é bissexto!')
