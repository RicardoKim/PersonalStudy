from making_random_list import random_list
import time

unsorted_list = random_list()

def selection_sort():
    start = time.process_time()
    list_length = len(unsorted_list)
    for i in range(list_length):
        min_value = unsorted_list[i]
        min_index = i
        for j in range(i + 1, list_length) :
            if min_value > unsorted_list[j] :
                min_value = unsorted_list[j]
                min_index = j
        if j != i :
            temp = unsorted_list[i]
            unsorted_list[i] = min_value
            unsorted_list[min_index] = temp
    end = time.process_time()
    print(unsorted_list, "Time : " , end - start)
    return

if __name__ == "__main__":
    selection_sort()