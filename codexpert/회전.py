import sys
sys.stdin = open("회전_input.txt")



n = int(input())

a = [[0 for _ in range(n)] for _ in range(n)]


for i in range(n):
    a[i] = list(map(int, input().split()))





for i in range(n):
    red = int(input())
    if red == 0:
        break

    if red == 90:
        b = [[0 for _ in range(n)] for _ in range(n)]
        for x in range(n):
            for y in range(n):
                b[y][n-1-x] = a[x][y]

        a = b

    elif red == 180:
        for j in range(2):
            b = [[0 for _ in range(n)] for _ in range(n)]
            for x in range(n):
                for y in range(n):
                    b[y][n-1-x] = a[x][y]

            a = b

    elif red == 270:
        for j in range(3):
            b = [[0 for _ in range(n)] for _ in range(n)]
            for x in range(n):
                for y in range(n):
                    b[y][n-1-x] = a[x][y]

            a = b

    elif red == 360:
        for j in range(4):
            b = [[0 for _ in range(n)] for _ in range(n)]
            for x in range(n):
                for y in range(n):
                    b[y][n-1-x] = a[x][y]

            a = b

    print('-----')



    for x in range(n):
        for y in range(n):
            print(b[x][y], end=" ")
        print()