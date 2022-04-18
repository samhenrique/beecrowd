n = int(input())
l = []
if n > 1 and n < 1000:
    l = input().split(" ")
    if len(l) == n:
        a = min(l)
        print("Menor valor: {}".format(a))
        for i in range(n):
            if a == l[i]:
                print("Posicao: {}".format(i + 1))
