# Author:ZERO


# Algo1
def brute_force_inversions(arr):
    n = len(arr)
    c = 0
    i = 0
    for i in range(n - 1):
        for j in arr[i:]:
            if arr[i] > j:
                c += 1
    return c


# Algo2 divide conquer
def inversions(arr):
    n = len(arr)
    if n == 1:
        return 0
    else:
        left = inversions(arr[:n // 2])
        right = inversions(arr[n // 2:])
        cross = count_split(arr)
        total = left + right + cross
    return total


def count_split(arr):
    n = len(arr)
    left = arr[:n // 2]
    left.sort()
    right = arr[n // 2:]
    right.sort()
    r = []
    i = 0
    j = 0
    c = 0
    for p in range(n):
        try:
            if left[i] < right[j]:
                r.append(left[i])
                i += 1
            else:
                r.append(right[j])
                j += 1
                c += len(left) - i
        except:
            pass
    return c


x = inversions([7, 1, 3, 5, 2, 6, 4])
y = brute_force_inversions([7, 1, 3, 5, 2, 6, 4])
print(x, y)
