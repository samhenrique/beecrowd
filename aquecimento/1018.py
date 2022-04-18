N = int(input())

if N < 1000000 and N > 0:

    print(N)

    cedulas = [100, 50, 20, 10, 5, 2, 1]

    for cedula in cedulas:
        cedulasquant = int(N/cedula)
        print("{} nota(s) de R$ ".format(cedulasquant), end="")
        print("{:.2f}".format(cedula).replace('.',','))
        N -= cedulasquant*cedula
