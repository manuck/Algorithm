import sys
sys.stdin = open("농작물수확_input.txt")

t = int(input())

for case in range(1):
    n = int(input())
    a = [[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        a[i] = list(input())

    res = 0
    mid = n//2
    for i in range(n):
        for j in range(n):
            if a[i][j].isdecimal():
                a[i][j] = int(a[i][j])


    print(a)
