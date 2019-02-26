import sys
sys.stdin = open("줄세우기_input.txt")

n = int(input())

st = list(range(1,n+1))
a = list(map(int, input().split()))

res = []
for i in range(n):
    res.insert(i-a[i],st[i])


for i in range(n):
    print(res[i], end=" ")

