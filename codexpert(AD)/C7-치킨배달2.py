import sys
sys.stdin = open("C7_input.txt")

def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    q = start[:]
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:continue
            if a[ny][nx] != 2 and visit[ny][nx] == 0:
                q.append((nx, ny))
                a[ny][nx] = a[y][x] + 1
                visit[ny][nx] = 1



n, m = map(int, input().split())
a = [[0 for _ in range(n)]for _ in range(n)]
visit = [[0 for _ in range(n)]for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
    print(a[i])


start = []
for i in range(n):
    for j in range(n):
        if a[i][j] == 2:
            start.append([j, i])
end = []
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            end.append([j, i])
print(end)
bfs()
print()
for i in range(n):
    print(a[i])
sol = 0
for i in range(len(end)):
    print(end[i][1], end[i][0])
    sol += (a[end[i][1]][end[i][0]]-2)
print(sol)
