nota = int(input("Insira a nota:"))
if nota >= 90:
    print(f"Conceito A")
else:
    if nota >= 80:
        print(f"Conceito B")
    else:
        if nota >= 70:
            print(f"Conceito D")
        else:
            if nota >= 60:
                print(f"Conceito E")
            else:
                print(f"Conceito F")