from making_random_list import random_list
import time

unsorted_list = random_list()

def merge_sort(arr):
    if len(arr) <= 1 :
        return arr
    else :
        mid = len(arr) // 2
        left = merge_sort(arr[0 : mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)

def merge(arr1, arr2) :
    if not arr1 :
        return arr2 
    elif not arr2 :
        return arr1
    else: 
        merged_list = []
        while arr1 and arr2 :
            v1 = arr1.pop(0)
            v2 = arr2.pop(0)
            if v1 < v2 :
                merged_list.append(v1)
                arr2 = [v2] + arr2
            else :
                merged_list.append(v2)
                arr1 = [v1] + arr1
        if arr1 :
            merged_list += arr1
        else :
            merged_list += arr2
        return merged_list

if __name__ == "__main__":
    print(unsorted_list)
    output = merge_sort(unsorted_list)
    print(output)