import sys
sys.stdin = open("B8_input.txt")

def powerset(n, k): # n: 원소의 갯수, k: 현재depth
    global res
    if n == k:      # basis part
        if sum(A) == n//2:
            sola = 0
            solb = 0
            for i in range(n):
                if A[i] == 1:
                    sola += a[i]
                elif A[i] == 0:
                    solb += a[i]
            if res > abs(sola-solb):
                res = abs(sola-solb)
    else:
        A[k] = 1
        powerset(n, k+1)
        A[k] = 0
        powerset(n, k+1)


n = int(input())
a = list(map(int, input().split()))
res = []
A = [0]*n
res = 999999
powerset(n, 0)
print(res)