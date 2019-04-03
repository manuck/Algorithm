import sys
sys.stdin = open("input(0403).txt")


def allpairsShortext():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                arr[i][j] = min(arr[i][k] + arr[k][j], arr[i][j])


t = int(input())
for case in range(1):
    li = list(map(int,input().split()))
    n = li.pop(0)
    # print(n)
    # print(li)
    arr = [[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if li[j + n*i] == 0 and i != j:
                arr[i][j] = 99999
            else:
                arr[i][j] = li[j + n*i]
    print(arr)
    allpairsShortext()
    # print(arr)

    res = 999999
    for i in range(n):
        if res > sum(arr[i]):
            res = sum(arr[i])
    print('#%i %i' % (case,res))