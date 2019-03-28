import sys
sys.stdin = open("최소합_input.txt")

dx = [0, 1]
dy = [1, 0]

def dfs(x, y, res):
    global n, flag, sol
    if sol:
        if min(sol) <= res:
            return

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if ny == n or nx == n: continue
        if ny == n-1 and nx == n-1:
            flag = 1
            if sol:
                if min(sol) > res:
                    sol.append(res)
            else:
                sol.append(res)
            res = 0
            break
        dfs(nx, ny, res + arr[ny][nx])

    if flag == 1:
        return res

t = int(input())
for case in range(1,t+1):
    n = int(input())
    arr = [[0 for _ in range(n)]for _ in range(n)]
    visited = [[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        arr[i] = list(map(int, input().split()))

    flag = 0
    sx, sy = 0, 0
    res = 0
    resmin = 888888
    sol = []
    dfs(sx, sy, res)

    print('#%i '%(case), end="")
    print(sol[-1]+arr[0][0]+arr[n-1][n-1])






