Cod1, Num1, Val1 = input().split(" ", 2)
Cod2, Num2, Val2 = input().split(" ", 2)
TOTAL = (int(Num1)*float(Val1))+(int(Num2)*float(Val2))
print("VALOR A PAGAR: R$ {:.2f}".format(TOTAL))