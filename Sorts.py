A = [5,2,3,1,4]
length = len(A)

for i in range(0,length-1):
    min_index = i
    for j in range(i+1,length):
        if(A[j]<A[min_index]):
            min_index = j
    if(min_index != i):
       temp = A[i]
       A[i] = A[min_index]
       A[min_index] = temp


print(A)
