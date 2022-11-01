from making_random_list import random_list
import time

unsorted_list = random_list()

def bubble_sort():
    start = time.process_time()
    list_length = len(unsorted_list)
    for i in range(list_length):
        for j in range(list_length - i - 1) :
            if unsorted_list[j] > unsorted_list[j + 1] :
                temp = unsorted_list[j]
                unsorted_list[j] = unsorted_list[j + 1]
                unsorted_list[j + 1] = temp
    end = time.process_time()
    print(unsorted_list, "Time : " , end - start)
    return

if __name__ == "__main__":
    bubble_sort()