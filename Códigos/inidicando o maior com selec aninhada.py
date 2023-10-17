a = int(input("Digite o número 1: "))
b = int(input("Digite o número 2: "))
c = int(input("Digite o número 3: "))
if a>b and a>c:
    print(f"O maior é {a}")
else:
    if b>a and b>c:
        print(f"O maior é {b}")
    else:
        if c>a and c>b:
            print(f"O maior é {c}")
            