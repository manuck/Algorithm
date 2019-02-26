import sys
sys.stdin = open("색종이배치_input.txt")


b = [[0 for _ in range(100)] for _ in range(100)]
a = [0 for _ in range(2)]
for i in range(2):
    a[i] = list(map(int, input().split()))

# print(a)
# print(b)
for k in range(2):
        for i in range(a[k][0], a[k][0]+a[k][2]+1):
            for j in range(a[k][1], a[k][1]+a[k][3]+1):
                b[i][j] += 1

# print(b)
cnt = 0
cnt2 = 0
for i in range(100):
    for j in range(100):
        if b[i][j] == 1:
            cnt += 1
        elif b[i][j] == 2:
            cnt2 += 1

xcnt=0
for i in range(100):
    for j in range(100):
        if b[i][j]==2:
            xcnt+=1
            break
ycnt=0
for i in range(100):
    for j in range(100):
        if b[j][i]==2:
            ycnt+=1
            break

# print(cnt)
if cnt2 == 1:
    print(1)
elif cnt2 == 0:
    print(4)

else:
    if xcnt>1 and ycnt>1:
        print(3)
    else:
        if cnt2!= 1:
            print(2)
