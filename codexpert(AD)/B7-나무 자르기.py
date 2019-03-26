import sys
sys.stdin = open("B7_input.txt")

n, m = map(int, input().split())
a = list(map(int,input().split()))

res = max(a)-1
# print(a, res)

while True:
    sol = 0
    for i in range(n):
        if res < a[i]:
            sol += a[i]-res

    if sol > n:
        print(max(a)-sol)
        break
    else:
        res -= 1