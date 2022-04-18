T = int(input())
F = [0,1]

for i in range(2, 61):
    F.append(F[i - 1] + F[i - 2])

for i in range(T):
    N = int(input())
    print("Fib({}) = {}".format(N, F[N]))