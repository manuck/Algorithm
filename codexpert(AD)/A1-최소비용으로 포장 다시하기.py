import sys
sys.stdin = open("A1_input.txt")

def BubbleSort_sort(n):   # O(n^2)
    # for k in range(n-1):
    for i in range(2):
        for j in range(i+1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]

n = int(input())
a = list(map(int, input().split()))
res = 0
a.sort()
while len(a) != 1:
    b = a.pop(0) + a.pop(0)
    res += b
    a.insert(0, b)
    # BubbleSort_sort(n-(1+len(a)))
    a.sort()

# print(a)
print(res)