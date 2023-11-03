
nota01=float(input("Digite a Primeira nota: "))
nota02=float(input("Digite a Segunda nota: "))
cont=0
media=(nota01+nota02)/2

if media >=7:
    print(f"Sua media é {media}, e você foi APROVADO!!")
elif media >=4:
    print(f"Sua media é {media}, e voccê está em RECUPERAÇÃO!!")
else:
    print(f"Sua media é {media}, e você foi REPROVADO!!")

print("Finalizado com sucesso.")