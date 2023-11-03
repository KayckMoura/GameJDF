time1=input("Digite o nome do time: ")
time2=input("Digite o nome do time: ")
marcados1=int(input(f"Digite quantos gols o time {time1} marcou: "))
marcados2=int(input(f"Digite quantos gols o time {time2} marcou: "))

if marcados1!=marcados2:
    if marcados1>marcados2:
        print(f"O time {time1} é o vencedor com {marcados1} pontos")
    else:
        print(f"O time {time2} é o vencedor com {marcados2} pontos")

else:
    print("Partida terminou em empate")