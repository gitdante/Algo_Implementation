def partition(arr,pivot):
    p=0
    bound=1
    for k in range(1,len(arr)):
        if arr[k] < p:
            if bound==k:
                bound+=1
            else:
                arr[k],arr[bound]=arr[bound],arr[k]
                bound+=1
    return arr[1:bound-1],arr[bound:]


def quick_sort(arr):
    if len(arr)==1:
        return arr[0]
    else:
        larr,rarr= partition(arr,0)
        l=quick_sort(larr)
        r=quick_sort(rarr)
        return l+r

