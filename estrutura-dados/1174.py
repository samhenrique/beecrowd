A=[]*100
for i in range(100):
    A.append(float(input()))
    
for j in range(100):
    if A[j] <= 10:
        print("A[{}] = {:.1f}".format(j, A[j]))
