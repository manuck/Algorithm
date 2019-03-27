import sys
sys.stdin = open("input(0327).txt")

def perm(n, k):
    global end, start, sol
    res = 0
    if n == k:
        res += abs(start[0]-cos[0][0])
        res += abs(start[1] - cos[0][1])
        if res >= sol:
            return
        res += abs(end[0] - cos[-1][0])
        res += abs(end[1] - cos[-1][1])
        if res >= sol:
            return
        for i in range(n-1):
            res += abs(cos[i][0]-cos[i+1][0])
            res += abs(cos[i][1]-cos[i+1][1])
            if res >= sol:
                break
        if sol > res:
            sol = res
    else:
        res += abs(start[0] - cos[0][0])
        res += abs(start[1] - cos[0][1])
        if res >= sol:
            return
        res += abs(end[0] - cos[-1][0])
        res += abs(end[1] - cos[-1][1])
        if res >= sol:
            return
        for i in range(k-1):
            res += abs(cos[i][0] - cos[i + 1][0])
            res += abs(cos[i][1] - cos[i + 1][1])
            if res >= sol:
                return
        for i in range(k, n):
            cos[i], cos[k] = cos[k], cos[i]
            perm(n, k+1)
            cos[i], cos[k] = cos[k], cos[i]


t = int(input())
for case in range(1, t+1):
    n = int(input())
    a = list(map(int, input().split()))

    start = [0]*2
    end = [0]*2
    cos = [0]*n
    sol = 1000000000

    start[0] = a.pop(0)
    start[1] = a.pop(0)
    end[0] = a.pop(0)
    end[1] = a.pop(0)

    for i in range(n):
        cos[i] = [a[2*i], a[(2*i)+1]]
    perm(n, 0)
    print('#%i %i' % (case, sol))