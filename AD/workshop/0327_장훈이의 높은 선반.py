import sys
sys.stdin = open("input(0327_2).txt")

def powerset(n, k, sum): # n: 원소의 갯수, k: 현재depth
    global b, res
    if sum >= res: return     # 가지치기
    if n == k:      # basis part
        sol = 0
        for i in range(n):
            if A[i] == 1:
                sol += data[i]
        if sol >= b:
            if res > sol:
                res = sol
    else:
        A[k] = 1
        powerset(n, k+1, sum + data[k])
        A[k] = 0
        powerset(n, k+1, sum)

t = int(input())
for case in range(1,t+1):
    n, b = map(int,input().split())
    data = list(map(int, input().split()))
    # print(data)
    # print(b)
    A = [0]*n
    res = 1000000000
    powerset(n, 0, 0)
    res -= b
    print('#%i %i'%(case, res))