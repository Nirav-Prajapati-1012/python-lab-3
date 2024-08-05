def sequential_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

arr = [1,3,5,8,10,23,35]
print(arr)
target = int(input("Search value : "))

result = sequential_search(arr, target)

if result != -1:
    print(f"Number {target} found at index {result}.")
else:
    print(f"Number {target} not found.")
