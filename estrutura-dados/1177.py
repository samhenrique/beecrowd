T = int(input())
N = []

if T > 2 and T < 50:

    j = 0
    
    for i in range(1,1001):

        if j == T:
            j = 0

        N.append(j)
        j = j + 1

    for j in range(1000):
        print("N[{}] = {}".format(j, N[j]))

