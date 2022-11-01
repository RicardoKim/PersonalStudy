from making_random_list import random_list
import time

unsorted_list = random_list()

def quick_sort(arr):
    if len(arr) <= 1 :
        return arr
    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]
    left_arr = []
    right_arr = []
    for value in arr :
        if value < pivot :
            left_arr.append(value)
        elif value > pivot :
            right_arr.append(value)
    
    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)

if __name__ == "__main__":
    output = quick_sort(unsorted_list)
    print(output)