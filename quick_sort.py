
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
def partition(arr,l,h):
    p=arr[l]
    i = l+1
    print(f'location of partition:{i}')
    # IMPORTANT!!!!
    # when using range and index together
    # you must be careful
    # range(4)=0,1,2,3
    # if l=0 h=3
    # then range(3)=0,1,3 !!!!!!!!!

    for j in range(l+1,h+1):
        if arr[j] < p:
            arr[j],arr[i]=arr[i],arr[j]
            print(arr)
            i+=1
    arr[(i-1)],arr[l]=arr[l],arr[(i-1)]
    return i-1

def swap(arr,a,b):
    return
def quick_sort(arr,l,h):
    if l>=h:
        return
    no= partition(arr,l,h)
    quick_sort(arr,l,no-1)
    quick_sort(arr,(no+1),h)

x=[7,1,4,33,2,5,8]
r=[1,2,4,5,7,8,33]
quick_sort(x,0,6)
print(x)