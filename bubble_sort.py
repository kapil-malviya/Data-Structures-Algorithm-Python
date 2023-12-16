def bubble_sort(arr):
	for i in range(len(arr)-1):
		print(arr) 
		for j in range(len(arr)-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [5, 8, 9, 12, -8, 7, 18]
bubble_sort(arr)
print(arr)
