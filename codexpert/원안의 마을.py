import sys
sys.stdin = open("원안의 마을_input.txt")

n = int(input())

a = [[0 for _ in range(n)]for _ in range(n)]
for i in range(n):
    a[i] = list(input())
    # print(a[i])

d = 0
xx=0
yy=0
for i in range(n):
    for j in range(n):
        if a[i][j]=='2':
            xx = j
            yy = i

for i in range(n):
    for j in range(n):
        if a[i][j] == '1':
            a[i][j] = '0'
            if d < ((j-xx)**2 + (i-yy)**2)**0.5:
                d = ((j-xx)**2 + (i-yy)**2)**0.5

# print()
# for i in range(n):
#     print(a[i])
# print(d)
print(round(d+0.49))


