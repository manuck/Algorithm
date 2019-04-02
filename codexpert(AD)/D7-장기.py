import sys
sys.stdin = open("D7_input.txt")

def bfs(x, y, cnt):
    global n, m, visited
    dx = [1, -1, 2, -2, 1, -1, 2, -2]
    dy = [2, 2, 1, 1, -2, -2, -1, -1]
    q = []
    q.append((x, y, cnt))
    visited[y][x] = 1
    while len(q) != 0:
        x, y, cnt = q.pop(0)
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if ny < 0 or ny >= m: continue
            if nx < 0 or nx >= n: continue
            if nx == ex and ny == ey:
                return cnt
            elif a[ny][nx] == 0 and visited[ny][nx] == 0:
                q.append((nx, ny, cnt+1))
                visited[ny][nx] = 1

    return cnt


n, m = map(int, input().split())

a = [[0 for _ in range(n)]for _ in range(m)]
visited = [[0 for _ in range(n)]for _ in range(m)]
sx, sy, ex, ey = map(int, input().split())
cnt = 1
# print(n, m)
# print(sx, sy, ex, ey)
# print(a)
res = bfs(sx, sy, cnt)
print(res)
