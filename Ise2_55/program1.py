# Find pair of elements whose sum is equal to given value
arr = [2, 7, 11, 15, 3, 6]
target = 9
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print("Pair:", arr[i], arr[j])
