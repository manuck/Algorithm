import sys
sys.stdin = open("미로의 거리_input.txt")



t = int(input())

for case in range(1):
    n = int(input())
    map = [[0 for _ in range(n)]for _ in range(n)]

    for i in range(n):
        map[i]=list(input())

    for i in range(n):
        print(map[i])