import sys
sys.stdin = open("A0_input.txt")

# def BubbleSort_sort(x):   # O(n^2)
#     for i in range(n-1):
#         for j in range(i+1, n):
#             if x[i] > x[j]:
#                 x[i], x[j] = x[j], x[i]

# def QuickSort(start, end):  # O(nLogn)
#     if start >= end:
#         return
#     P = end # pivot
#     T = start   # target
#     for L in range(start, end+1):
#         if a[L] < a[P]:
#             a[L], a[T] = a[T], a[L]
#             T += 1
#     a[T], a[P] = a[P], a[T]
#     QuickSort(start, T-1)
#     QuickSort(T+1, end)

def MergeSort(start, end):
    global a, temp
    if start >= end:
        return

    m = (start + end) // 2
    MergeSort(start, m)
    MergeSort(m+1, end)
    i = start
    j = m + 1
    k = start
    while i <= m and j <= end:   # 왼쪽영역, 오른쪽영역을 나누어서 임시버퍼에 비교한후 저장
        if a[i] < a[j]:
            temp[k] = a[i]
            k += 1
            i += 1
        else:
            temp[k] = a[j]
            k += 1
            j += 1
    while i <= m:   # 왼쪽영역이 남아있으면 임시버퍼에 저장
        temp[k] = a[i]
        k += 1
        i += 1
    while j <= end: # 오른쪽영역이 남아있으면 임시버퍼에 저장
        temp[k] = a[j]
        k += 1
        j += 1

    for i in range(start, end+1):
        a[i] = temp[i]


n = int(input())
a = list(map(int, input().split()))

start = 0
end = n-1
temp = [0]*(n)
# a.sort()
# QuickSort(start, end)
# BubbleSort_sort(a)
MergeSort(start, end)

for i in a:
    print(i, end=" ")