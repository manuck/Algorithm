import sys
sys.stdin = open("섬_input.txt")

# t = int(input())
#
# for case in range(1,t+1):
#     n = int(input())
#     a = [[0 for _ in range(n)]for _ in range(n)]
#
#     for i in range(n):
#         a[i] = list(map(int, input().split()))
#         # print(a[i])
#
#     cnt = 0
#     hmax = 0
#     # 높이 최대
#     for i in range(n):
#         for j in range(n):
#             if hmax < a[i][j]:
#                 hmax = a[i][j]
#
#     for i in range(n):
#         for j in range(n):
#             if i >= 0 and j > 0:
#                 if a[i][j] != 0:
#                     if a[i + 1][j] == 0 and a[i][j - 1] == 0:
#                         cnt += 1
#
#     print('#', end="")
#     print(str(case), end=" ")
#     print(cnt, end=" ")
#     print(hmax)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    global ans
    q = [(x,y)]
    while len(q):
        x,y = q.pop(0)

        if ans < mat[x][y] : ans = mat[x][y]
        mat[x][y] = 0

        for i in range(4):
            newX, newY = x + dx[i], y + dy[i]
            if 0 <= newX < n and 0 <= newY < n and mat[newX][newY]:
                    q.append((newX, newY))


def dfs(x, y):
    global ans
    if ans < mat[x][y] : ans = mat[x][y]
    mat[x][y] = 0
    for i in range(4):
        newX, newY = x + dx[i], y + dy[i]
        if 0 <= newX < n and 0 <= newY < n and mat[newX][newY]:
            dfs(newX, newY)

t = int(input())
for case in range(1, t+1):
    n = int(input())

    mat = [0 for i in range(n)]
    for i in range(n):
        mat[i] = list(map(int, input().split()))

    ans = 0
    cnt = 0
    for i in range(n):
        for j in range(n):
            if mat[i][j]:
                #bfs(i,j)
                dfs(i,j)
                cnt += 1
    print("#%i %i" %(case, cnt))