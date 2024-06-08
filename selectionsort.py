import time


def selectsort(A):
    compare = 0
    assingment = 0
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            compare+=1
            if A[min_idx] > A[j]:
                min_idx = j
                        
        A[i], A[min_idx] = A[min_idx], A[i]
        assingment+=1
    return compare,assingment

arr = []
f = open("test20k.txt", "r")
for x in f:
    if x.strip():
        n = int(x)
        arr.append(n)
print("Sorting...")
start = time.time()  
compare,assingment = selectsort(arr)
end = time.time()



print("sorted\n")
print("Sample size: 20000")
print("Total comparison: ",compare," \nTotal assingment: ",assingment)



print(end - start,"seconds")
