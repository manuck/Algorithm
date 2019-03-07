import sys
sys.stdin = open("노드의 합_input.txt")


t = int(input())
for case in range(1,t+1):
    N, M, L = map(int, input().split())
    a = [[0 for _ in range(2)]for _ in range(M)]
    for i in range(M):
        a[i] = list(map(int, input().split()))

    b = [0]*(N+1)
    # print(a)
    for i in range(M):
        b[a[i][0]] = a[i][1]
    num = N
    # print(b)
    # print(num//2)
    while b.count(0) != 1:
        if num % 2 == 1:
            b[num//2] = b[num] + b[num-1]
            num = num - 2
        else:
            b[num // 2] = b[num]
            num = num - 1

        # print(b)
        b[0] = 0
    print('#', end="")
    print(str(case), end=" ")
    print(b[L])
