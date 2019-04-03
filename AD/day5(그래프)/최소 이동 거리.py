import sys
sys.stdin = open("최소신장트리_input.txt")

def allpairsShortext():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                arr[i][j] = min(arr[i][k] + arr[k][j], arr[i][j])

t = int(input())
for case in range(1):
    n, e = map(int, input().split())
    arr = [[0 for _ in range(n+1)]for _ in range(n+1)]
    g = [[0 for _ in range(n+1)]for _ in range(n+1)]
    for i in range(e):
        n1, n2, w = list(map(int, input().split()))
        arr[n1][n2] = w
        g[n1][n2] = w
    for i in range(n+1):
        for j in range(n+1):
            if i != j and arr[i][j]==0:
                arr[i][j] = 999999999

    print(arr)
    allpairsShortext()
    print(arr)
    res = 999999
    for i in range(n):
        if res > sum(arr[i]):
            res = sum(arr[i])
    print('#%i %i' % (case, res))