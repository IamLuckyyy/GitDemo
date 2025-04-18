def mergeSort(list1):

    # Dividing the list
    if len(list1)>1:
        mid = len(list1)//2
        left_list = list1[:mid]
        right_list = list1[mid:]
        mergeSort(left_list)
        mergeSort(right_list)
        i = 0
        j = 0
        k = 0

        # Merging
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list1[k] = left_list[i]
                i = i + 1
                k = k + 1
            else:
                list1[k] = right_list[j]
                j = j + 1
                k = k + 1

        # Check any value left in the Left sub-list
        while i < len(left_list):
            list1[k] = left_list[i]
            i = i + 1
            k = k + 1

        # Check any value left in the Right sub-list
        while j < len(right_list):
            list1[k] = right_list[j]
            j = j + 1
            k = k + 1

num = int(input("Enter the lenght of list:"))
list1 = [ int(input()) for x in range(num) ]
mergeSort(list1)
print("Sorted list is:",list1)