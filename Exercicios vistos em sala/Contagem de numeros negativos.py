cont=0
menor=cont
for x in range(5):
    n=int(input("Digite um número:"))
    if n >= 0:
        cont=+1
    else:
        print(n)
print(f"Numeros negativos: {cont}, e eles são: {menor}")