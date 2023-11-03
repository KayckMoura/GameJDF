tipo=input("Tipo de combustivel G ou E")
litros=float(input("Digite quantos litros deseja"))

if tipo == "E"or tipo == "e":
    total=litros*4.90

elif tipo == "G" or tipo == "g":
    total=litros*5.80

else:
    print("Tipo de combustivel invalido")
    total=0
print(f"O valor gasto foi {total}")