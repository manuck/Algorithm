import sys
sys.stdin = open("A4_input.txt")

# def lowerSearch(s, e, data):
#     sol = -1
#     while s <= e:
#         m = (s+e)//2
#         if arr[m] >= data:
#             e = m - 1
#             sol = m
#         else:
#             s = m + 1
#     return sol
#
# def upperSearch(s, e, data):    # 오른쪽 상한치 위치 탐색
#     sol = -1
#     while s <= e:
#         m = (s+e)//2
#         if data >= arr[m]:
#             s = m + 1
#             sol = m
#         else:
#             e = m - 1
#     return sol
#
# n = int(input())
# arr = []
# for i in range(n):
#     arr.append(int(input()))
# arr.sort()
#
# cnt = 0
#
# for i in range(n-2):
#     for j in range(i+1, n-1):
#         dist = arr[j] - arr[i]
#         start = arr[j] + dist
#         end = arr[j] + dist*2
#         lo = lowerSearch(j+1, n-1, start)
#         if lo == -1 or arr[lo] > end:
#             continue
#         up = upperSearch(j+1, n-1, end)
#         cnt += (up-lo+1)
# print(cnt)






def upperSearch(s, e, data):    # 오른쪽 상한치 위치 탐색
    sol = -1
    while s <= e:
        m = (s+e)//2
        if data > arr[m]:
            s = m + 1
            sol = m + 1
        else:
            e = m - 1
    return sol

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()
print(arr)
res = 0
jump = 0

for i in range(0, n-1):
    for j in range(i+1, n):
        jump = arr[j] - arr[i]
        # print(upperSearch(0, n-1, arr[j]+2*jump+1))
        # print(upperSearch(0, n-1, arr[j]+jump))
        res += upperSearch(0, n-1, arr[j]+2*jump+1) - upperSearch(0, n-1, arr[j]+jump)
print(res)

# for i in range(n-2):
#     for j in range(i+1,n-1):
#         jump1 = arr[j] - arr[i]
#         for k in range(j+1, n):
#             jump2 = arr[k] - arr[j]
#             if jump2 < jump1:
#                 continue
#             elif jump2 > 2*jump1:
#                 break
#             else:
#                 res += 1
# print(res)

