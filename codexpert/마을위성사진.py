import sys
sys.stdin = open("마을위성사진_input.txt")

n = int(input())
# b = [[0 for _ in range(n)] for _ in range(n)]
a = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    a[i] = list(input())

# print(a)
flag=1

while flag!= 0:
    flag=0
    xindex = []
    yindex = []

    for i in range(1, n-1):
        for j in range(1,n-1):
            if int(a[i][j])>0:
                if a[i][j]==a[i+1][j] and a[i][j]==a[i-1][j] and a[i][j]==a[i][j+1] and a[i][j]==a[i][j-1]:
                    xindex.append(j)
                    yindex.append(i)
                    flag=1

    for i in range(len(xindex)):
        a[yindex[i]][xindex[i]] = int(a[yindex[i]][xindex[i]])+1

res = 0
for i in range(1, n - 1):
    for j in range(1, n - 1):
        if res < int(a[i][j]):
            res= int(a[i][j])
print(res)
