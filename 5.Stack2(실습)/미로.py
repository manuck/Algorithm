import sys
sys.stdin = open("미로_input.txt")


t = int(input())
for case in range(1):
    n = int(input())
    G = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        G[i] = list(input())

    for x in range(n):
        for y in range(n):
            if G[y][x]=='3':
                yi = y
                xi = x
    print(yi,xi)
