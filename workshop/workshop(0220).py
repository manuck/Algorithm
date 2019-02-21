import sys
sys.stdin = open("0220_input.txt")

for case in range(1,11):
    N = int(input())
    a = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        a[i] = list(map(int, input().split()))
    # print(a)
    cnt = 0
    for x in range(N):
        li = []

        for y in range(N):
            if a[y][x] != 0:
                li.append(a[y][x])
        # print(li)
        i = 0
        while li[i] != 1:
            li[i] = 0
            i += 1
        # print(li)
        j = 0
        while li[~j] != 2:
            li[~j] = 0
            j += 1

        for c in range(len(li)):
            if c!=len(li) and li[c]==1:
                if li[c+1]==2:
                    cnt += 1
        # print(cnt)
    print(f'#{case} {cnt}')





