import sys
sys.stdin = open("Q1_input.txt")

def bfs(x, y, cnt):

    dx = [-3,-2,2,3,-3,-2,2,3]
    dy = [2,3,3,2,-2,-3,-3,-2]
    q =[]
    q.append((x, y, cnt))
    visited[y][x] = 1
    while q:
        # print(q)
        x, y, cnt = q.pop(0)
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
            if nx == ex and ny == ey:
                # print(cnt)
                return cnt
            if visited[ny][nx] == 0:
                q.append((nx, ny, cnt+1))
                visited[ny][nx] = 1
    return 0

t = int(input())

for case in range(1, t+1):
    n = int(input())
    visited = [[0 for _ in range(n)]for _ in range(n)]
    sx, sy, ex, ey = map(int,input().split())
    cnt = 1
    # print(n)
    # print(sx, sy, ex, ey)
    sol = bfs(sx,sy,cnt)

    print('#%i %i' % (case,sol))