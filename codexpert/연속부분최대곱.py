import sys
sys.stdin = open("연속부분최대곱_input.txt")

n = int(input())
a = []
for i in range(n):
    a.append(float(input()))

# res = 0
# for i in range(n):
#     m = 1
#     if a[i] >= 1:
#         for j in range(i, n):
#             if a[j] * m > res:
#                 res = m*a[j]
#             m *= a[j]
#
# print('%.3f' %res)


mul = 1.0
res = 0.0
# for i in range(n):
#     mul = 1.0
#     for j in range(1, n):
#         mul *= a[j]
#         if mul > res:
#             res = mul



for i in range(n):
    if mul * a[i] < a[i]:
        mul = a[i]
    else:
        mul *= a[i]
    if mul > res:
        res = mul

print('%.3f' %res)