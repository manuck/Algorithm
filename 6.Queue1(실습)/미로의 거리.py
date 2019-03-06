import sys
sys.stdin = open("미로의 거리_input.txt")



# t = int(input())
#
# for case in range(1):
#     n = int(input())
#     map = [['1' for _ in range(n+2)]for _ in range(n+2)]
#
#     for i in range(1, n+1):
#         map[i] = ['1'] + list(input()) + ['1']
#
#     # for i in range(n+2):
#     #     print(map[i])
#
#     xi = 0
#     yi = 0
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if map[i][j]=='3':
#                 yi = i
#                 xi = j
#     xx = xi
#     yy = yi
#     dy = [1, -1, 0, 0]
#     dx = [0, 0, -1, 1]
#     dindex = 0
#     cnt = 0
#     # print(yi, xi)
#     cc = 0
#     index=[]
#     while True:
#         check = 0
#         for i in range(4):
#             if i == 0 and map[yi-1][xi] == '0':
#                 check += 1
#             elif i == 1 and map[yi+1][xi] == '0':
#                 check += 1
#             elif i == 2 and map[yi][xi+1] == '0':
#                 check += 1
#             elif i == 3 and map[yi][xi-1] == '0':
#                 check += 1
#
#         if check >= 2:
#             index.append(yi)
#             index.append(xi)
#
#
#         xi += dx[dindex]
#         yi += dy[dindex]
#
#         if map[yi][xi] == '0':
#             cnt += 1
#             map[yi][xi] = '1'
#
#         elif map[yi][xi] == '1':
#             xi -= dx[dindex]
#             yi -= dy[dindex]
#             dindex += 1
#             cc += 1
#             if dindex == 4:
#                 dindex = 0
#
#         elif map[yi][xi] == '3':
#             dindex += 1
#             if dindex == 4:
#                 dindex = 0
#
#         elif map[yi][xi] == '2':
#             break
#
#
#         # if cc > 10000:
#         #     cnt = 0
#         #     break
#         if yi == yy and xi == xx:
#             cc += 1
#
#         if cc > 6:
#             xi = index[1]
#             yi = index[1]
#             break
#
#
#     result = ''
#     result += '#'
#     result += str(case)
#     result += ' '
#     result += str(cnt)
#     print(result)


def bfs(x, y):
    global N, maze, visited
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = []
    q.append((x, y))  # 리스트로 큐 구현, 좌표는 튜플로 저장
    visited[x][y] = 1  # 방문 표시
    while len(q) != 0:
        x, y = q.pop(0)  # deQ
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ny < 0 or ny == N: continue
            if nx < 0 or nx == N: continue
            if maze[nx][ny] == 3:  # 출구인 경우 지나온 칸 반환
                return visited[x][y] - 1  # 출발지는 칸 수에서 제외
            elif maze[nx][ny] == 0 and visited[nx][ny] == 0:  # 갈수 있는 곳 저장
                q.append((nx, ny))  # enQ
                visited[nx][ny] = visited[x][y] + 1
    return 0  # 출구에 가지 못하고 모든 칸 방문


T = int(input())
for tc in range(T):
    N = int(input())
    maze = [[int(x) for x in input()] for i in range(N)]  # 미로를 중첩리스트로 저장
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):  # 출발점 찾기
        for j in range(N):
            if maze[i][j] == 2:
                x, y = i, j
    print('#{} {}'.format(tc + 1, bfs(x, y)))