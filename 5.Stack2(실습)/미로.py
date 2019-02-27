import sys
sys.stdin = open("미로_input.txt")

goal = False
arr = []


def dfs(x, y):
    global arr, n
    global goal

    if x - 1 >= 0:
        if arr[x - 1][y] == 0:
            arr[x - 1][y] = -1
            dfs(x - 1, y)
        elif arr[x - 1][y] == 3:
            goal = True
            return
    if y - 1 >= 0:
        if arr[x][y - 1] == 0:
            arr[x][y - 1] = -1
            dfs(x, y - 1)
        elif arr[x][y - 1] == 3:
            goal = True
            return
    if x + 1 < n:
        if arr[x + 1][y] == 0:
            arr[x + 1][y] = -1
            dfs(x + 1, y)
        elif arr[x + 1][y] == 3:
            goal = True
            return
    if y + 1 < n:
        if arr[x][y + 1] == 0:
            arr[x][y + 1] = -1
            dfs(x, y + 1)
        elif arr[x][y + 1] == 3:
            goal = True
            return


t = int(input())
for case in range(1, t + 1):
    n = int(input())
    arr = [list() for x in range(n)]
    for x in range(n):
        line = input()
        for y in range(n):
            arr[x].append(int(line[y]))

    start_x = 0
    start_y = 0
    out_break = False
    for x in range(n):
        for y in range(n):
            if arr[x][y] == 2:
                start_x = x
                start_y = y
                out_break = True
                break
        if out_break:
            break

    goal = False
    dfs(start_x, start_y)

    if goal:
        print(f'#{case} {1}')
    else:
        print(f'#{case} {0}')