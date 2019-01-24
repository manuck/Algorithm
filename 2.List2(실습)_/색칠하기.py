import sys
sys.stdin = open("색칠하기_input.txt")

t = int(input())
for q in range(t):
    n = int(input())

    a = [[0 for _ in range(5)] for _ in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    # print(a)

    arr = [[0 for _ in range(10)] for _ in range(10)]
    for k in range(n):
        for i in range(a[k][0],a[k][2]+1):
            for j in range(a[k][1],a[k][3]+1):
                arr[i][j] += 1
    # print(arr)
    cnt = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j]==2:
                cnt += 1

    print(f'#{q+1} {cnt}')