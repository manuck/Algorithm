import sys
sys.stdin = open("배열최소합_input.txt")

t = int(input())
for case in range(1, t+1):
    n = int(input())
    arr = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        arr[i] = list(map(int, input().split()))


