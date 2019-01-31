import sys
sys.stdin = open("문자열 비교_input.txt")

def BruteForce(p, t):
    i = 0
    j = 0
    M = len(p)
    N = len(t)
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1

    if j == M:
        return 1
    else:
        return 0

t = int(input())
for case in range(t):
    A = str(input())
    B = str(input())
    r = BruteForce(A, B)
    print(f'#{case+1} {r}')