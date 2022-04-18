X = float(input())
N = []

for i in range(100):
    N.append(X)
    X = X/2
    Y = N[i]
    print("N[{}] = {:.4f}".format(i, Y))