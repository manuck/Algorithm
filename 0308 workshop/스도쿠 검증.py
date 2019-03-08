import sys
sys.stdin = open("스도쿠 검증_input.txt")

t = int(input())

for case in range(1,t+1):

    a = [[0 for _ in range(9)]for _ in range(9)]

    numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        a[i] = list(map(int, input().split()))
        # print(a[i])

    xcnt=0
    garo = 1
    res = 1
    for j in range(9):
        for i in range(9):
            if numlist[i] not in a[j]:
                res = 0

    for q in range(9):
        sero = []
        for j in range(9):
            for i in range(9):
                sero.append(a[i][q])

            if numlist[j] not in sero:
                res = 0

    for i in range(0,7,3):
        for j in range(0,7,3):
            # print(i)
            # print(j)
            sq = []
            for y3 in range(3):
                for x3 in range(3):
                    sq.append(a[y3+i][x3+j])

            for q in range(9):
                if numlist[q] not in sq:
                    res = 0
    print('#', end="")
    print(str(case), end=" ")
    print(res)



