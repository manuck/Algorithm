import sys
sys.stdin = open("전자카트_input.txt")

def perm(n, k):
    sol = 0
    fir = 0
    if n == k:
        b = a[:]
        b.append(1)
        for i in b:
            sol += arr[fir][i-1]
            fir = i-1
        res.append(sol)

    else:
        for i in range(k, n):
            a[i], a[k] = a[k], a[i]
            perm(n, k+1)
            a[i], a[k] = a[k], a[i]

t = int(input())
for case in range(1,t+1):
    n = int(input())
    arr = [[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        arr[i] = list(map(int, input().split()))
        # print(arr[i])
    a = list(range(2, n+1))
    # print(a)
    res = []
    perm(n-1, 0)
    ans = min(res)
    print('#%i %i' % (case, ans))
