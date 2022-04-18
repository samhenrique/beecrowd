A, B = input().split(" ", 1)
A = int(A)
B = int(B)

precos = [4.0, 4.5, 5.0, 2.0, 1.5]

A += 1

total = precos[A]*B
print(total)
print("Total: R$ {:.2f}".format(total))
