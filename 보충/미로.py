import sys
sys.stdin = open("미로_input.txt")

goal = False
arr = []


def dfs(x, y):
    global arr
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
    if x + 1 < 16:
        if arr[x + 1][y] == 0:
            arr[x + 1][y] = -1
            dfs(x + 1, y)
        elif arr[x + 1][y] == 3:
            goal = True
            return
    if y + 1 < 16:
        if arr[x][y + 1] == 0:
            arr[x][y + 1] = -1
            dfs(x, y + 1)
        elif arr[x][y + 1] == 3:
            goal = True
            return


for case in range(1,11):
    n = int(input())
    arr = [list() for x in range(16)]
    # print(arr)
    for x in range(16):
        line = input()
        for y in range(16):
            arr[x].append(int(line[y]))
            # print(arr[x])
    start_x = 1
    start_y = 1
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
        print('#', end="")
        print(case, end=" ")
        print('1')
    else:
        print('#', end="")
        print(case, end=" ")
        print('0')