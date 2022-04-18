A, B, C = input().split(" ", 2)
a = float(A)
b = float(B)
c = float(C)

delta = (b**2)-(4.0*a*c)

if delta < 0 or a < 0:
    print("Impossivel calcular")

else:
    R1 = (-b+(float(delta)**0.5))/(2.0*a)
    R2 = (-b-(float(delta)**0.5))/(2.0*a)
    print("R1 = {:.5f}".format(R1))
    print("R2 = {:.5f}".format(R2))