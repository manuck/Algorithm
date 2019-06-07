n = int(input())

a = list(map(int, input().split()))
a.sort()
sol = 0
ans = 0
for i in a:
    # print(i)
    sol += i
    ans += sol
print(ans)