cont=0
for x in range(10):
    n=int(input("Digite um número:"))
    if n>=10 and n<=20:
        cont+=1
        print(f"Este número está dentro do intervalo, {n}")

print(f"Números dentro do intervalo: {cont}")