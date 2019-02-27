import sys
sys.stdin = open("창고다각형_input.txt")



n = int(input())

a = [[0 for _ in range(2)] for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
a.sort()
print(a)


ymax=0
index=0
for i in range(n):
    if a[i][1]>ymax:
        ymax=a[i][1]
        index = i


res = 0
for i in range(index):
    if a[i][1] > a[i+1][1]:
        a[i+1][1] = a[i][1]
        res += a[i][1] * (a[i + 1][0] - a[i][0])
    else:
        res += a[i][1]*(a[i+1][0]-a[i][0])

for i in range(n-1, index, -1):

    if a[i][1] > a[i-1][1]:
        a[i-1][1] = a[i][1]
        res += a[i][1]*(a[i][0]-a[i-1][0])
    else:
        res += a[i][1] * (a[i][0]-a[i-1][0])

res = res+ymax
print(res)


# xmax = 0
# ymax = 0
# for i in range(n):
#     if a[i][0] > xmax:
#         xmax = a[i][0]
#
# for i in range(n):
#     if a[i][1] > ymax:
#         ymax = a[i][1]
#
# base = [[0 for _ in range(xmax+1)] for _ in range(ymax+1)]
#
# for k in range(n):
#     for i in range(a[k][0], a[k][0]+1):
#         for j in range(a[k][1]):
#             base[j][i] += 1
#
# # for i in range(ymax+1):
# #     print(base[i])
#
# cnt = 0
# yst = 0
# xst = 0
# for i in range(xmax+1):
#     for j in range(ymax+1):
#         if base[j][i] == 1:
#             if yst < j:
#                 yst = j
#                 xst = i
#
# # print(yst, xst)
#
# # print()
# for i in range(xst, xmax+1):
#     xyo = 0
#     yyo = 0
#     for j in range(ymax+1):
#         if base[j][i] == 1:
#             if j > yyo:
#                 # j = y, i = x
#                 for q in range(xst, i):
#                     for w in range(0, j+1):
#                         base[w][q] = 1
#
# for i in range(0, xst+1):
#     xyo = 0
#     yyo = 0
#     for j in range(ymax+1):
#         if base[j][i] == 1:
#             if j > yyo:
#                 for q in range(i, xst):
#                     for w in range(0, j+1):
#                         base[w][q] = 1
#
# for i in range(ymax+1):
#     for j in range(xmax+1):
#         if base[i][j] == 1:
#             cnt += 1
#
# # for i in range(ymax+1):
# #     print(base[i])

# print(cnt)

