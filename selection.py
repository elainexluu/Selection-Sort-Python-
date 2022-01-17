# In selction sort, the unsorted array will be parsed until it finds the smallest value. Once the smallest value in the unsorted array has been found, it will be swapped with the first element. This will continue until the array has been sorted increasingly.

arr = [5, 3, 8, 2, 4, 1, 9, 7, 6]

min = arr[0]

# find the smallest element
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        curr = arr[i+1]

        if curr < min:
            # update min
            min = arr[j]

            # swap the min with the position you STARTED the search
            startIndex = arr.index(5)
            minIndex = arr.index(1)

            arr[startIndex],  arr[minIndex] = arr[minIndex], arr[startIndex]


print("min: " + str(min))
print(arr)
