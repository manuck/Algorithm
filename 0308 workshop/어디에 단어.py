import sys
sys.stdin = open("어디에 단어_input.txt")

t = int(input())

for case in range(1):
    n, k = list(map(int, input().split()))

    a = [[0 for _ in range(n)]for _ in range(n)]

    for i in range(n):
        a[i] = list(map(int, input().split()))
        print(a[i])

    res = 0
    # for i in range(n):
    #     for j in range(n):
    #         if a[i][j]==1:
    #             for q in range(n-j):



    print('#', end="")
    print(case, end=" ")
    print(res)


