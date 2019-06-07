n = int(input())

num = list(map(int, input()))
ans = 0
for i in range(len(num)):
    ans += num[i]

print(ans)