# In selction sort, the unsorted array will be parsed until it finds the smallest value. Once the smallest value in the unsorted array has been found, it will be swapped with the first element. This will continue until the array has been sorted increasingly.

arr = [5, 3, 8, 2, 4, 1, 9, 7, 6]


# find the smallest element
for i in range(len(arr)):

    # assign min as the first element in the array
    min = i

    for j in range(i+1, len(arr)):
        curr = arr[j]

        if curr < arr[min]:
            # update min
            min = j

    # swap the min with the position you STARTED the search
    arr[i],  arr[min] = arr[min], arr[i]

# display
print(arr)
