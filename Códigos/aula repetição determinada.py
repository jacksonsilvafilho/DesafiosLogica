#exemplo de somatório, no valor de soma substitua por um valor inteiro.

soma = 0
num = int(input("Num: "))
for cont in range(1,num+1):
    soma = soma + cont
print(f"Somatório: {soma}")
