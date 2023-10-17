temp = int(input("Informe a temperatura: "))
umd = int(input("Informe a umidade do ar: "))

if temp>=30 and umd>=60:
    print(f"Quente e úmido.")
else: 
    if temp>=30 and umd<=60:
        print(f"Quente")
        