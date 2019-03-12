import sys
sys.stdin = open("미로_input.txt")

def bfs(x, y):
    global N, maze, visited
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = []
    q.append((x, y))
    visited[x][y] = 1
    while len(q) != 0:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ny < 0 or ny == 16: continue
            if nx < 0 or nx == 16: continue
            if maze[nx][ny] == 3:
                return 1
            elif maze[nx][ny] == 0 and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = 1
    return 0

for case in range(1):
    N = int(input())
    maze = []
    for i in range(16):
        maze.append(list(map(int, list(input()))))
    visited = [[0 for _ in range(16)] for _ in range(16)]
    # print(maze)
    # print(visited)
    print('#{} {}'.format(case, bfs(1, 1)))