import sys
sys.stdin = open("A6_input.txt")

col, row = map(int, input().split())
sc, sr, ec, er = map(int, input().split())
table = []
dx = [-1, 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1]

for x in range(row):
    table.append(list(map(int, list(input()))))
# print(table)

def BFS():
    que = []
    # 1. 시작점을 큐에 저장(방문표시)
    que.append([sr, sc, 0])
    table[sr][sc] = 1 # 방문
    while len(que) != 0: # 큐가 빌때까지 반복
        r, c, time = que.pop(0)
        if r == er and c == ec:
            return time
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if (nr < 1 or nc < 1 or nr > row or nc > col):
                continue
            if table[nr][nc] != 0:
                continue
            if table[nr][nc] != 0:
                continue
            que.append([nr, nc, time + 1])
            table[nr][nc] = 1 # 방문
    return -1

# X, Y = map(int, input().split())
# mapindex = list(map(int, input().split()))
# maze = []
# for i in range(Y):
#     maze.append(list(map(int, input())))
#     print(maze[i])
#
# visited = [[0 for _ in range(X)]for _ in range(Y)]

print(BFS())

