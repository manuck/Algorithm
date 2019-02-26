n = int(input())
score = [0]*n

a = [[0 for _ in range(3)] for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))

for i in range(3):
    for j in range(n):
        flag=0
        for k in range(n):
            if j != k:
                if a[j][i] == a[k][i]:
                    flag = 1
                    break
        if flag==0:
            score[j] += a[j][i]

for i in range(len(score)):
    print(score[i])