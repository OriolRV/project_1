import datetime
import random

def merge_lists(list1,list2,merged):
    p1 = 0
    p2 = 0
    pmerged = 0
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] <= list2[p2]:
            merged[pmerged] = list1[p1]
            p1 += 1
        else:
            merged[pmerged] = list2[p2]
            p2 += 1
        pmerged += 1
    
    while p1 < len(list1):
        merged[pmerged] = list1[p1]
        p1 += 1
        pmerged += 1
        
    while p2 < len(list2):
        merged[pmerged] = list2[p2]
        p2 += 1
        pmerged += 1
        
    

def merge_sort(numbers_list):

    if len(numbers_list) == 1:
        return
    else:
        middle_point = len(numbers_list) // 2
        left_list = numbers_list[:middle_point]
        right_list = numbers_list[middle_point:] 
        merge_sort(left_list)
        merge_sort(right_list)
        merge_lists(left_list,right_list,numbers_list)


l = [random.randint(0,100) for i in range(10000000)]
merge_sort(l)
