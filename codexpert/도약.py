import sys
sys.stdin = open("도약_input.txt")

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort()
# print(a)
cnt = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        jump1 = a[j]-a[i]
        for k in range(j+1, n):
            jump2 = a[k]-a[j]
            if jump2 < jump1:
                continue
            elif jump2 > jump1*2:
                break
            else:
                cnt += 1
print(cnt)