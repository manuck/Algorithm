import sys
sys.stdin = open("ladder2_input.txt")


for case in range(1,11):
    n = int(input())

    a = [[0 for _ in range(100)]for _ in range(100)]
    # print(a)
    for i in range(100):
        a[i] = [0]+list(map(int, input().split()))+[0]

    # dx = [-1, 1, 0]
    # dy = [0, 0, 1]

    li = []
    res = []


    mcnt = 999
    while True:
        x = 0
        y = 0

        xcnt = 0
        for i in range(102):
            if a[0][i] == 1:
                # print(i, end=" ")
                xcnt += 1

        if xcnt == 0:
            break

        for i in range(102):
            if a[0][i] == 1:
                x = i-1
                a[0][i] = 0
                y += 1
                break

        cnt = 1
        # print(x, y)
        li.append([x, y])
        while y != 99:
            if a[y][x+1] == 1:
                while a[y][x+1] != 0:
                    x += 1
                    cnt += 1
                    # print(x,y)
            elif a[y][x-1] == 1:
                while a[y][x-1] != 0:
                    x -= 1
                    cnt += 1


            y += 1
            cnt += 1
        if mcnt > cnt:
            mcnt = cnt
            res = li.pop()
        elif mcnt == cnt:
            res = li.pop(0)
        elif mcnt < cnt:
            li.pop()



    #     print(cnt)
    # print(li)
    print('#', end="")
    print(case, end=" ")
    print(res[0])