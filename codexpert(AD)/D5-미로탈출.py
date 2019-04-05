import sys
sys.stdin = open("D5_input.txt")

def bfs():
    global x, y
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    q = []
    q.append((x, y, 0))
    visited[y][x] = 0
    while q:
        x, y, cnt = q.pop(0)
        for i in range(4):
            nr = y + dr[i]
            nc = x + dc[i]
            if a[nr][nc] == 1: continue
            if a[nr][nc] == 4: return cnt+1
            if a[nr][nc] == 2:
                if visited[y][x] >= 3: continue
                if visited[nr][nc] > visited[y][x] + 1:
                    q.append((nc, nr, cnt+1))
                    visited[nr][nc] = visited[y][x] + 1
            elif a[nr][nc] == 0:
                if visited[nr][nc] > visited[y][x]:
                    q.append((nc, nr, cnt+1))
                    visited[nr][nc] = visited[y][x]
    return -1

r, c = map(int, input().split())    # r = 세로크기, c = 가로크기
a = [[0 for _ in range(c)]for _ in range(r)]
visited = [[9 for _ in range(c)]for _ in range(r)]

for i in range(r):
    a[i] = list(map(int, input().split()))
    # print(a[i])

for i in range(r):
    for j in range(c):
        if a[i][j] == 3:
            y = i
            x = j

# print(x, y)
# print(ex, ey)
res = bfs()
print(res)