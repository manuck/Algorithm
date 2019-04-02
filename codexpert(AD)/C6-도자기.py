import sys
sys.stdin = open("C6_input.txt")

def comb(n, r, q):
    # 가지치기 조건
    global res, sol
    if r == 0:
        # print(T)
        if sorted(T) not in res:
            res.append(sorted(T))
            sol += 1
    elif n < r:
        return
    else:
        T[r-1] = A[n-1]
        comb(n-1, r-1, q)
        comb(n-1, r, q)

def dfs(start, cnt):
    global sol, n, m, A, rec
    if cnt == m:
        # for i in range(cnt):
        #     print(rec[i], end=" ")
        # print()
        sol += 1
        return
    if start >= n: return
    back = 0
    for i in range(start, n):   # start부터 끝까지 재료를 담아보는 시도
        if back == A[i]: continue
        rec[cnt] == A[i]
        back = A[i]
        dfs(i+1, cnt+1)

t = int(input())
for case in range(t):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    rec = [0] * n
    A.sort()
    # print(A)
    # print(n)
    T = [0] * n
    sol = 0
    res = []
    # comb(n, m, 2)
    dfs(0, 0)
    print(sol)
