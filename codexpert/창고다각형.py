import sys
sys.stdin = open("창고다각형_input.txt")

base = [[0 for _ in range(1000)] for _ in range(1000)]

n = int(input())

a = [[0 for _ in range(2)] for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))

print(a)

for k in range(n):
    for i in range(a[k][0], a[k][0]+1):
        for j in range(a[k][1]):
            base[i][j] += 1

cnt = 0
yst = 0
xst = 0
for i in range(1000):
    for j in range(1000):
        if base[i][j] == 1:
            if yst < j:
                yst = j
                xst = i

print(yst, xst)
flag = 1

for i in range(xst,1000):
    xx=0
    yy=0
    for j in range(1000):
        if base[i][j]==1:
            if yy < j:
                for q in range(xst, xx):
                    for w in range(yy):
                        base[q][w] = 1
print(base)
cnt = 0
for i in range(1000):
    for j in range(1000):
        if base[i][j] == 1:
            cnt+=1
print(cnt)