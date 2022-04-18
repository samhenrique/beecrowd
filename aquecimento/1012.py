A, B, C = input().split(" ", 2)
pi = 3.14159
ATri = float(A)*float(C)/2.0
ACir = pi*(float(C)**2.0)
ATra = (float(A)+float(B))*float(C)/2.0
AQua = float(B)**2.0
ARet = float(A)*float(B)
print("TRIANGULO: {:.3f}".format(ATri))
print("CIRCULO: {:.3f}".format(ACir))
print("TRAPEZIO: {:.3f}".format(ATra))
print("QUADRADO: {:.3f}".format(AQua))
print("RETANGULO: {:.3f}".format(ARet))