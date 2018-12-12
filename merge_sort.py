def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    else:
        larr = merge_sort(arr[:n // 2])
        rarr = merge_sort(arr[n // 2:])
        return merge(larr, rarr)


def merge(larr, rarr):
    ln = len(larr)
    rn = len(rarr)
    r = []
    i, j, k = (0, 0, 0)
    for k in range(ln + rn):
        if larr[i] < rarr[j]:
            r[k] = larr[i]
            i += 1
        else:
            r[k] = rarr[j]
            j += 1
    return r
