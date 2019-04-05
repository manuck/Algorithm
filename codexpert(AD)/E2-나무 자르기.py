import sys
sys.stdin = open("E2_input.txt")

# n, m = map(int, input().split())
# a = list(map(int,input().split()))
#
# a.sort(reverse=True)
# # print(a)
# res = a[0]-1
# # print(a, res)
#
# while True:
#     sol = 0
#     for i in range(n):
#         if sol >= m:
#             break
#         if res >= a[i]:
#             break
#         else:
#             sol += a[i]-res
#
#     if sol >= m:
#         print(res)
#         break
#     else:
#         res -= 1

N, M = map(int, input().split())
trees = sorted([int(x) for x in input().split()], reverse=True)
MAX = sum(trees)
# print(trees)
# print(MAX)
start = 0
end = trees[0]
find = False
result = 0

while start <= end:
    mid = (start + end) // 2
    total = MAX
    for i in range(N):
        if trees[i] >= mid:
            total -= mid
        else:
            total -= trees[i]

    if total == M:
        find = True
        result = mid
        break

    if M < total:
        start = mid + 1
    else:
        end = mid - 1

if not find:
    result = (start + end) >> 1
print(result)

'''
N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort(reverse=True)
MAX = sum(trees)
# print(trees)
# print(MAX)
start = 0
end = trees[0]
find = 0
result = 0

while start <= end:
    mid = (start + end) // 2
    total = MAX
    for i in range(N):
        if trees[i] >= mid:
            total -= mid
        else:
            total -= trees[i]

    if total == M:
        result = mid
        break

    if M < total:
        start = mid + 1
    else:
        end = mid - 1

print(result)'''