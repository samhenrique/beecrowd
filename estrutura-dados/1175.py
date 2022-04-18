N = []
a = 0
b = 0

while a < 20:
    N.append(int(input()))
    a = a + 1

M = list(reversed(N))

while b < 20:
     
    print("N[{}] = {}".format(b,M[b]))
    b = b + 1