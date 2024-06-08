import time
compare = 0
assingment = 0

def merge(arr, l, m, r):
    global assingment
    global compare
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        compare += 1
        assingment += 1
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        compare += 1
        assingment += 1
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        compare += 1
        assingment += 1
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
 
def mergeSort(arr, l, r):
    global compare
    global assingment
    assingment += 1
    if l < r:
        m = l+(r-l)//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
 
 


arr = []
f = open("test20k.txt", "r")
for x in f:
    if x.strip():
        n = int(x)
        arr.append(n)
print("Sorting...")
n = len(arr)

 
start = time.time()  
mergeSort(arr,0,n-1)
end = time.time()



print("sorted\n")
print("Sample size: 20000")
print("Total comparison: ",compare," \nTotal assingment: ",assingment)



print(end - start,"seconds")
