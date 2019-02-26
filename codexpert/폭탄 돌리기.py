import sys
sys.stdin = open("폭탄 돌리기_input.txt")

k = int(input())
n = int(input())

a = [[0 for _ in range(2)] for _ in range(n)]
for i in range(n):
    a[i] = list(map(str, input().split()))


res = 0
index = k

for i in range(n):
    res += int(a[i][0])

    if res > 210:
        break
    if a[i][1] == 'P' or a[i][1] == 'F':
        continue

    else:
        index += 1

    if index == 9:
        index = 1

print(index)