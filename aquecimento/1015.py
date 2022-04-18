X1, Y1 = input().split(" ", 1)
X2, Y2 = input().split(" ", 1)
x1 = float(X1)
y1 = float(Y1)
x2 = float(X2)
y2= float(Y2)

distancia = ((x2-x1)**2+(y2-y1)**2)**0.5
print("{:.4f}".format(distancia))