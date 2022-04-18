A, B, C = input().split(" ", 2)
a = int(A)
b = int(B)
c = int(C)

MaiorAB = (a+b+abs(a-b))/2
MaiorBC = (c+b+abs(c-b))/2

if MaiorAB>MaiorBC:
    final = MaiorAB

else:
    final = MaiorBC
    
print(int(final),"eh o maior")