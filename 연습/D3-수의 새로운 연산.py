import sys
sys.stdin = open("수의 새로운 연산_input.txt")

t = int(input())

for case in range(1):
    a, b = map(int, input().split())
    print(a, b)
    n = 0
    if a >= b:
        n = int(a**(1/2))+1
    else:
        n = int(b**(1/2))+1
    print(n)
    arr = [[0 for _ in range(n+1)]for _ in range(n+1)]

    for i in range(1, n):
        num = i-1
        for j in range(1, n):
            arr[j][i] = num + i
            num += j

    for i in range(n):
        print(arr[i])