import time

def bubbleSort(arr):
    compare = 0
    assingment = 0
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            compare+=1
            if arr[j] > arr[j + 1] :
                assingment += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return compare,assingment
 
arr = []
f = open("test1k.txt", "r")
for x in f:
    if x.strip():
        n = int(x)
        arr.append(n)
print("Sorting...")

start = time.time()  
compare,assingment = bubbleSort(arr)
end = time.time()

print(arr)


print("sorted\n")
print("Total comparison: ",compare," \nTotal assingment: ",assingment)



print(end - start,"seconds")