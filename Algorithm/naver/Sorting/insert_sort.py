from making_random_list import random_list

unsorted_list = random_list()

def insertion_sort():
    for end in range(1, len(unsorted_list)):
        for i in range(end, 0, -1):
            if unsorted_list[i - 1] > unsorted_list[i]:
                temp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[i - 1]
                unsorted_list[i - 1] = temp
            else :
                break
    print(unsorted_list)
    return 

if __name__ == "__main__":
    insertion_sort()