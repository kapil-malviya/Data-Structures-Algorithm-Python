def sum_list(arr):
    if not arr:
        return 0
    else:
        return arr[0] + sum_list(arr[1:])

my_list = [1, 2, 3, 4, 5]
result = sum_list(my_list)
print(result)  # Output: 15







