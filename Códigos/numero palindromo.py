numero = int(input('Informe um número inteiro de 4 dígitos:'))
if numero<1111 or numero>9999: print('Valor informado inválido! Não tem 4 dígitos')
else:
    milhar = numero//1000
    resto = numero%1000
    centena = resto//100
    resto = resto%100
    dezena = resto//10
    unidade = resto%10
    invertido = unidade * 1000 + dezena * 100 + centena * 10 + milhar
    print('Valor ao contrário: ', invertido)
    if numero==invertido: print('Número Palíndromo')
    else: print("Número não é Palíndromo")