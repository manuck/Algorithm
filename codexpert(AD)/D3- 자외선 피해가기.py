import sys
sys.stdin = open("D3_input.txt")

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def bfs():
    q = []
    q.append((0, 0))
    visited[0][0] = arr[0][0]
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
            # 가볼위치의 이전의 해 > 현재진행경로의 해 비교하여 최소이면
            if visited[ny][nx] > visited[y][x] + arr[ny][nx]:
                q.append((nx, ny))
                visited[ny][nx] = visited[y][x] + arr[ny][nx]



n = int(input())
arr = [[0]]*n

visited = [[100000 for _ in range(n)]for _ in range(n)]
for i in range(n):
    arr[i] = list(input())
for i in range(n):
    for j in range(n):
        if arr[i][j].isdecimal():
            arr[i][j] = int(arr[i][j])

bfs()
print(visited[n-1][n-1])