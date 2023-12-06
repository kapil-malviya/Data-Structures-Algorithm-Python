def selection_sort(lst):
    n = len(lst)
    
    for i in range(n):
        min_index = i
        
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        
        # Swap the minimum element with the current element
        lst[i], lst[min_index] = lst[min_index], lst[i]

lst = [10,8,5,4,3,1,2]
selection_sort(lst)
print(lst)