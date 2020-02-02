A = [12, 1, 23, 4, 34, 11, 49]
def insertionSort(A):
  length=len(A)
  for j in range(1,length):
    key=A[j]
    i=j-1
    while i>-1 and A[i]>key:
      A[i+1]=A[i]
      i=i-1
    A[i+1]=key

  print(A)
insertionSort(A)

def selectionSort(A):
 for i in range(0,len(A)-1):
    index_min = i
    for j in range(i+1, len(A)):
        if(A[j] <  A[index_min]):
            index_min = j
            if(index_min != i):
                temp = A[i]
                A[i] = A[index_min]
                A[index_min] = temp

selectionSort(A)
print(A)

def bubbleSort(A):
 for i in range(0,len(A)):
    for j in range(1,len(A)):
        if A[j] < A[j-1]:
            temp = A[j]
            A[j] = A[j-1]
            A[j-1] = temp
bubbleSort(A)
print(A)

def mergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2
        left = A[:mid]
        right = A[mid:]
        mergeSort(left)
        mergeSort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1

mergeSort(A)
print(A)

def countingSort(A):
    def partition(a, p, r):
        x = a[r]
        i = p - 1
        for j in range(p, r):
            if a[j] <= x:
                i = i + 1
                t = a[i]
                a[i] = a[j]
                a[j] = t
        t = a[i + 1]
        a[i + 1] = a[r]
        a[r] = t
        return i + 1

    def q_sort(a, p, r):
        if (p < r):
            q = partition(a, p, r)
            q_sort(a, p, q - 1)
            q_sort(a, q + 1, r)

    p = 0
    a = [2, 8, 7, 1, 3, 5, 6, 4]
    r = len(a) - 1
    q_sort(a, p, r)
    print(a)
    countingSort(a)

