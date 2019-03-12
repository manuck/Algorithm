import sys
sys.stdin = open("미로_input.txt")

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    maze[y][x] = 9  # 방문표시

    for i in range(4):
        global flag
        nx = x + dx[i]
        ny = y + dy[i]
        if maze[ny][nx] == 3:
            flag = 1
            break
        if maze[ny][nx] == 0:  # 함수를 넣어서 갈 수 있는 것만 통과
            dfs(nx, ny)
    if flag == 1:
        return 1
    else:
        return 0

for case in range(1, 11):
    tc = input()
    maze = []
    flag = 0
    old = []
    for i in range(16):
        maze.append(list(map(int, list(input()))))
    print("%s%d %d" % ('#', case, dfs(1, 1)))