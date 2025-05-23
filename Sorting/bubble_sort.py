# Python program for implementation of Bubble Sort
def bubbleSort(arr,n):

    for i in range(n-1): # range(n) also work but outer loop will repeat one time more than needed.

        # traverse the array from 0 to n-i-1
        for j in range(0, n-i-1): # Last i elements are already in place

            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)
bubbleSort(arr,n)

print ("Sorted array is:") 
for i in range(len(arr)):
    print("%d" % arr[i],end=" ")