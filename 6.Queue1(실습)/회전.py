import sys
sys.stdin = open("회전_input.txt")

t = int(input())

for case in range(1,t+1):
    N, M = list(map(int, input().split()))
    a = list(map(int, input().split()))

    for i in range(M):
        b = a.pop(0)
        a.append(b)

    print(f'#{case} {a[0]}')