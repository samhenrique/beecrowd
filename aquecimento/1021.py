N = float(input())

if 0 <= N and N <= 1000000.00:

    cedulas = [100, 50, 20, 10, 5, 2]
    moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

    print("NOTAS:")
    for cedula in cedulas:
        cedulasquant = int(N/cedula)
        print("{} nota(s) de R$ {:.2f}".format(cedulasquant, cedula))
        N -= cedulasquant*cedula

    print("MOEDAS:")
    for moeda in moedas:
        moedasquant = int(N/moeda)
        print("{} moeda(s) de R$ {:.2f}".format(moedasquant, moeda))
        N -= moedasquant*moeda

else:
    exit()