arr = [5, 2, 7, 1, 3, 8, 9, 3, 5, 2]

def recselectionsort(ary, s, e):
    mini = s
    if s == e: return
    for j in range(s+1, e , 1):
        if arr[j] < ary[mini]:
            mini=j

    ary[s], ary[mini] = ary[mini], ary[s]

    recselectionsort(ary, s+1, e)


recselectionsort(arr, 0, 10)
print(arr)