L = int(input())
matriz = []
tamanho = 12

if L >= 0 and L <= 11:
    T = input()
    if T == "S":
        for i in range(tamanho):
            linha = []
            for j in range(tamanho):
                linha.append(float(input()))
            matriz.append(linha)
        for k in range(tamanho):
            soma = soma + k

    elif T == "M":
        a = 2

    else:
        exit()
