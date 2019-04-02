import sys
sys.stdin = open("Q3_input.txt")

def bfs1(x, y):
    a = [[0 for _ in range(100)] for _ in range(100)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = []
    cnt = 1
    q.append((x, y, cnt))
    while q:
        x, y, cnt = q.pop(0)
        # print(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= 100 or ny >= 100: continue
            for j in range(int(len(r)/2)):
                if nx == r[2*j] and ny == r[2*j+1]:
                    r.pop(2*j)
                    r.pop(2*j)
                    return cnt
            if a[ny][nx] == 0:
                q.append((nx, ny, cnt+1))
                a[ny][nx] = 1
    return 0

def bfs2(x, y):
    a = [[0 for _ in range(100)] for _ in range(100)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = []
    cnt = 1
    q.append((x, y, cnt))
    while q:
        x, y, cnt = q.pop(0)
        # print(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= 100 or ny >= 100: continue
            for j in range(int(len(r2)/2)):
                if nx == r2[2*j] and ny == r2[2*j+1]:
                    r2.pop(2*j)
                    r2.pop(2*j)
                    return cnt
            if a[ny][nx] == 0:
                q.append((nx, ny, cnt+1))
                a[ny][nx] = 1
    return 0


t = int(input())
for case in range(1, t+1):
    n = int(input())
    s = list(map(int, input().split()))
    r = list(map(int, input().split()))

    res = 0
    res2 = 0
    r2 = r[:]
    #

    for k in range(n):
        # print((s[2*k], s[2*k+1]))
        z = bfs1(s[2*k], s[2*k+1])
        res2 += z

    for k in range(n-1,-1,-1):
        # print((s[2*k], s[2*k+1]))
        z = bfs2(s[2*k], s[2*k+1])
        res += z
        # print(r)
    print('#%i ' % (case),end="")
    if res2<res:
        print(res2)
    else:
        print(res)