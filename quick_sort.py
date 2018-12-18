import numpy as np

"""
Partition (A,l,r) [ input corresponds to A[l...r]] -
    p:= A[l]
    i:= l+1
    for j=l+1 to r
        if A[j] < p
            swap A[j] and A[i]
            i:= i+1
    swap A[l] and A[i-1]
"""

c = 0


def partition(arr, l, h):
    global c
    c += h - l
    print(c)
    p = arr[l]
    i = l + 1
    # IMPORTANT!!!!
    # when using range and index together
    # you must be careful
    # range(4)=0,1,2,3
    # if l=0 h=3
    # then range(3)=0,1,3 !!!!!!!!!

    for j in range(l + 1, h + 1):
        if arr[j] < p:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[(i - 1)], arr[l] = arr[l], arr[(i - 1)]
    return i - 1


def chose_pivot(arr, l, h, t):
    if t == 0:
        return l
    if t == 1:
        return h
    else:
        return median_of_three(arr, l, h)


def quick_sort(arr, l, h):
    if l >= h:
        return
    posi = chose_pivot(arr, l, h, 2)
    posi = int(posi)
    arr[posi], arr[l] = arr[l], arr[posi]
    no = partition(arr, l, h)
    quick_sort(arr, l, no - 1)
    quick_sort(arr, (no + 1), h)


def median_of_three(arr, l, h):

    m = 0 if (h - l) == 1 else (h - l) // 2 + l
    M = arr[m]  # middle element
    L = arr[l]  # leftmost element
    H = arr[h]  # rightmost element
    ordered = sorted([(L, l), (M, m), (H, h)])
    return ordered[1][1]  # index of median of the three


x = [7, 1, 4, 33, 2, 5, 8]
r = [1, 2, 4, 5, 7, 8, 33]
nubarr = [int(i) for i in open('QuickSort.txt')]
quick_sort(nubarr, 0, len(nubarr) - 1)

[]
