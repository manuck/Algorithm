import sys
sys.stdin = open("섬_input.txt")

t = int(input())

for case in range(1,t+1):
    n = int(input())
    a = [[0 for _ in range(n)]for _ in range(n)]

    for i in range(n):
        a[i] = list(map(int, input().split()))
        # print(a[i])

    cnt = 0
    hmax = 0
    # 높이 최대
    for i in range(n):
        for j in range(n):
            if hmax < a[i][j]:
                hmax = a[i][j]

    for i in range(n):
        for j in range(n):
            if i >= 0 and j > 0:
                if a[i][j] != 0:
                    if a[i + 1][j] == 0 and a[i][j - 1] == 0:
                        cnt += 1

    print('#', end="")
    print(str(case), end=" ")
    print(cnt, end=" ")
    print(hmax)



    # li = []
    # cnt1 = 0
    # cnt2 = 0
    # cnt3 = 0
    # cnt4 = 0
    # for i in range(n):
    #     for j in range(n):
    #         if i > 0 and j > 0 and i< n-1 and j < n-1:
    #             if a[i][j] == 0:
    #                 if a[i - 1][j-1] != 0:
    #                     cnt1 += 1
    #                 if a[i+1][j+1]!=0:
    #                     cnt2 +=1
    #                 if a[i+1][j-1]!=0:
    #                     cnt3 +=1
    #                 if  a[i - 1][j + 1] != 0:
    #                     cnt4 += 1
    # li.append(cnt1)
    # li.append(cnt2)
    # li.append(cnt3)
    # li.append(cnt4)
    # print(li)




    # if i >= 0 and j > 0:
    #     if a[i][j] != 0:
    #         if a[i + 1][j] == 0 and a[i][j - 1] == 0:
    #             cnt += 1

    # if x > 0 and x < n and y > 0 and y < n:
    #     x = x + dx[index]
    #     y = y + dy[index]
    # else:
    #     index += 1
    #
    # if a[y][x] == 0:
    #     y -= dy[index]
    #     x -= dx[index]
    # elif a[y][x] != 0:
    #     a[y][x] = 0
    # for i in range(n):
    #     print(a[i])