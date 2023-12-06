def merge_sort(arr):
    if len(arr) <= 1:
        return arr  

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_sorted_lists(left, right)

def merge_two_sorted_lists(a, b):

    len_a = len(a)
    len_b = len(b)
    i = j = 0
    
    merged = []

    while i < len_a and j < len_b:

        if a[i] < b[j]:
            merged.append(a[i])
            i += 1

        else:
            merged.append(b[j])
            j += 1

    merged.extend(a[i:])
    merged.extend(b[j:])

    return merged


arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print('sorted_arr : ',sorted_arr)