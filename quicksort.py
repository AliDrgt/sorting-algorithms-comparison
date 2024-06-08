import time
compare = 0
assingment = 0


def partition(arr, low, high):
    global assingment
    global compare
    i = (low-1)       
    pivot = arr[high]     
    for j in range(low, high):  
        compare +=1
        if arr[j] <= pivot:
            i = i+1
            assingment+=1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
 
 
def quickSort(arr, low, high):
    global assingment
    global compare
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
 
 

arr = []
f = open("test20k.txt", "r")
for x in f:
    if x.strip():
        n = int(x)
        arr.append(n)
print("Sorting...")
n = len(arr)

start = time.time()
quickSort(arr, 0, n-1)
end = time.time()

# print(arr)


print("sorted\n")
print("Sample size: 20000")
print("Total comparison: ",compare," \nTotal assingment: ",assingment)



print(end - start,"seconds")

