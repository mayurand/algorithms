'''
Created on 30 Nov 2016

@author: Mayur Andulkar
'''
import math

def merge(list_2b_sorted,start,break_point,end):
    n1 = break_point-start+1
    n2 = end-break_point
    
    part_1 = []
    part_2 = []
    for i in range(n1):
        part_1.append(list_2b_sorted[start+i]) # This runs from start to break_point
    for j in range(n2):
        part_2.append(list_2b_sorted[break_point+j+1])  # This runs from break_point+1 to end  
    
    part_1.append(float("inf"))
    part_2.append(float("inf"))
    
    i = j =0
    for index in range(start,end+1): # end+1 because the range will give from start to end-1
        if part_1[i]<=part_2[j]:
            list_2b_sorted[index]=part_1[i]
            i = i + 1 # Keeping track of the index of part_1
        else:
            list_2b_sorted[index]=part_2[j]
            j = j + 1 # Keeping track of the index of part_2

    return list_2b_sorted

def mergeSort(list_2b_sorted,start,end):
    if start<end:
        mid_pt = int(math.floor((start+end)/2))
        mergeSort(list_2b_sorted, start, mid_pt)
        mergeSort(list_2b_sorted, mid_pt+1, end)
        merge(list_2b_sorted, start, mid_pt, end)
        
    return list_2b_sorted


alist = [2,4,5,7,1,2,3,6,9]            
print(mergeSort(alist,0,7))