import sys
sys.stdin = open("0227_input.txt")

t = int(input())


for case in range(1,t+1):
    n = int(input())
    total = 0
    a = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))

    li = []
    for i in range(n):
        for j in range(n):
            x = 0
            y = 0
            if a[i][j] != 0:
                # print(i, j)
                total+=1

                for w in range(n-i):
                    if a[i+w][j] == 0:
                        y = w
                        li.append(y)
                        break

                for k in range(n-j):
                    if a[i][j+k] == 0:
                        x = k
                        li.append(x)
                        break



                for q in range(i, i+y+1):
                    for e in range(j, j+x+1):
                        a[q][e] = 0

    # print(li)

    front = []
    back = []
    for i in range(len(li)):
        if i%2==0:
            front.append(li[i])
        else:
            back.append(li[i])


    # print(front)
    # print(back)
    res = []
    for i in range(len(front)):
        res.append([front[i]*back[i], front[i], back[i]])

    res.sort()
    res.sort()
    print(f'#{case}', end=" ")
    print(total, end=" ")
    for i in range(len(res)):
        print(res[i][1], end=" ")
        print(res[i][2], end=" ")

    print()