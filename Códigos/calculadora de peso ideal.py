altura = float(input('Informe a altura:  '))
genero = int(input('Informe o genero, usando 1 para feminino e 2 para masculino: '))
if genero==1 : peso = 62.1 * altura - 44.7
if genero==2 : peso = 72.7 * altura - 58
if genero!=1 and genero!=2 :
    print('Gênero inválido! Peso ideal inválido.')
    peso = 0
print('Peso ideal: ' , peso)