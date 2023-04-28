def quickSort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)


array = [4, 2, 9, 6, 23, 12, 34, 0, 1]
sorted_array = quickSort(array)
print(sorted_array)