import sys
sys.stdin = open("B6_input.txt")

def powerset(n, k): # n: 원소의 갯수, k: 현재depth
    global res
    if n == k:      # basis part
        sol = 0
        for i in range(n):
            if A[i] == 1:
                sol += a[i]
        if sol >= b and res > sol:
            res = sol
    else:
        A[k] = 1
        powerset(n, k+1)
        A[k] = 0
        powerset(n, k+1)

t = int(input())
for case in range(t):
    n, b = map(int, input().split())
    # print(n, b)
    a = [0]*n
    for i in range(n):
        a[i] = int(input())
    res = 999999999
    A = [0 for _ in range(n)]
    # print(a)
    powerset(n, 0)
    print(res-b)



