import timeit
import random

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged



if __name__ == '__main__':
    data_small = [random.randint(0, 1000) for _ in range(1000)]
    data_medium = [random.randint(0, 10000) for _ in range(10000)]
    data_big = [random.randint(0, 100000) for _ in range(100000)]
    
    time_small_insertion_sort = timeit.timeit(lambda: insertion_sort(data_small[:]), number = 10)
    time_small_merge_sort = timeit.timeit(lambda: merge_sort(data_small[:]), number = 10)
    time_small_Tim_sorted = timeit.timeit(lambda: sorted(data_small[:]), number = 10)
    time_small_Tim_sort = timeit.timeit(lambda: data_small[:].sort(), number = 10)

    time_medium_insertion_sort = timeit.timeit(lambda: insertion_sort(data_medium[:]), number = 10)
    time_medium_merge_sort = timeit.timeit(lambda: merge_sort(data_medium[:]), number = 10)
    time_medium_Tim_sorted = timeit.timeit(lambda: sorted(data_medium[:]), number = 10)
    time_medium_Tim_sort = timeit.timeit(lambda: data_medium[:].sort(), number = 10)

    time_big_insertion_sort = timeit.timeit(lambda: insertion_sort(data_big[:]), number = 10)
    time_big_merge_sort = timeit.timeit(lambda: merge_sort(data_big[:]), number = 10)
    time_big_Tim_sorted = timeit.timeit(lambda: sorted(data_big[:]), number = 10)
    time_big_Tim_sort = timeit.timeit(lambda: data_big[:].sort(), number = 10)

    print(f"{'Algoritm': <20} | {'Time small data': <20} | {'Time medium data': <20} | {'Time big data': <20}")
    print(f":{'-'*19} | :{'-'*19} | :{'-'*19}| :{'-'*19}")
    print(f"{'Insertion sort': <20} | {time_small_insertion_sort: <20.5f} | {time_medium_insertion_sort: <20.5f}| {time_big_insertion_sort: <20.5f}")
    print(f"{'Merge sort': <20} | {time_small_merge_sort: <20.5f} | {time_medium_merge_sort: <20.5f}| {time_big_merge_sort: <20.5f}")
    print(f"{'Tim_sorted': <20} | {time_small_Tim_sorted: <20.5f} | {time_medium_Tim_sorted: <20.5f}| {time_big_Tim_sorted: <20.5f}")
    print(f"{'Tim_sort': <20} | {time_small_Tim_sort: <20.5f} | {time_medium_Tim_sort: <20.5f}| {time_big_Tim_sort: <20.5f}")


#Results:
#Algoritm             | Time small data      | Time medium data    | Time big data       
#:------------------- | :------------------- | :-------------------| :-------------------
#Insertion sort       | 0.20011              | 20.61421            | 2302.84658
#Merge sort           | 0.01869              | 0.20852             | 2.77295
#Tim_sorted           | 0.00077              | 0.01132             | 0.16811
#Tim_sort             | 0.00071              | 0.01094             | 0.16068
#PS C:\Projects_goit\Algorithm\goit-algo-hw-04> 

#Tim_sort method is the most faster