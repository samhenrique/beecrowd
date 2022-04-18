par = []
impar = []
c = 0
i = 0
p = 0
n = 0

while c < 15:
    n = int(input())
    if n%2 == 0:
        par.append(n)
        p = p + 1
    else:
        impar.append(n)
        i = i + 1

    if p > 4:

        for j in range(5):
            print("par[{}] = {}".format(j, par[j]))
        par = []
        p = 0

    if i > 4:
        for k in range(5):
            print("impar[{}] = {}".format(k, impar[k]))
        impar = []
        i = 0
        c = c + 1

    if i>0:
        for j in range(i):
            print('impar[{}] = {}'.format(j,impar[j]))
    if p>0:
        for h in range(p):
            print('par[{}] = {}'.format(h,par[h]))