import sys
sys.stdin = open("x모양_input.txt")

t = int(input())

for case in range(1, t+1):
    N, K = map(int, input().split())

    a = [[0 for _ in range(N)]for _ in range(N)]

    for i in range(N):
        a[i] = list(map(int, input().split()))
        # print(a[i])

    res = 999

    for i in range(N-K+1):
        for j in range(N-K+1):
            lsum = 0
            rsum = 0
            for y in range(K):
                lsum += a[i+y][j+y]


            for x in range(K):
                rsum += a[i+K-1-x][j+x]

            # print(lsum, rsum)

            if rsum > lsum:
                if res >= rsum-lsum:
                    res = rsum-lsum
            else:
                if res >= lsum - rsum:
                    res = lsum - rsum

    print('#', end="")
    print(str(case), end=" ")
    print(res)