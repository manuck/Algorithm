import sys
sys.stdin = open("D8_input.txt")

def bfs():
    global visited, b
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = []
    for i in range(len(start)):
        q.append(start[i])
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or ny >= n or nx >= m :continue

            if a[ny][nx] != -1 and a[ny][nx] == 0 and visited[ny][nx] == 0:
                q.append((nx, ny))
                a[ny][nx] = a[y][x]+1
                visited[ny][nx] = 1

m, n = map(int, input().split())
a = [[0 for _ in range(m)]for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    a[i] = list(map(int, input().split()))

start = []
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            start.append([j, i])

bfs()

sol = 0
flag = 0

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            flag = -1
        if a[i][j] > sol:
            sol = a[i][j]

if flag == 0:
    print(sol-1)
elif flag == -1:
    print(-1)




