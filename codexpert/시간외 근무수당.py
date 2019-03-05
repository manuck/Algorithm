import sys
sys.stdin = open("시간외 근무수당_input.txt")

a = [[0 for _ in range(2)]for _ in range(5)]

for i in range(5):
    a[i] = list(map(float, input().split()))

# print(a)

sumtime = 0
for i in range(5):
    if a[i][1]-a[i][0] < 5 and a[i][1]-a[i][0] > 1:
        sumtime += a[i][1]-a[i][0] - 1
    elif a[i][1]-a[i][0] >= 5:
        sumtime += 3

# print(sumtime)
restime = sumtime * 2
sol = restime * 5000

if sumtime >= 15:
    sol*0.95
elif sumtime <= 5:
    sol*1.05

print(int(sol))
