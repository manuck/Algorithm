import sys
sys.stdin = open("회문_input.txt")

t = int(input())
for case in range(t):
    N , M = map(int, input().split())
    a = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        a[i]  = list(input())
    res = ''

    for y in range(N):
        for x in range(N-M+1):
            if a[y][x:(x+M)] == a[y][x:(x+M)][::-1]:
                res = a[y][x:(x+M)]

    for x in range(N):
        li = []
        for y in range(N):
            li.append(a[y][x])
            # if a[y:(y+M)][x] == a[y:(y+M)][x][::-1]:
            #     res = a[y:(y+M)][x]
        for i in range(len(li)-M+1):
            if li[i:(i+M)] == li[i:(i+M)][::-1]:
                res = li[i:(i+M)]
    res = ''.join(res)
    print(f'#{case+1} {res}')