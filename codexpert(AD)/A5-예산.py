import sys
sys.stdin = open("A5_input.txt")

# def my_budget(a):
#     sol = 0
#     for i in range(n):
#         if arr[i] < a:
#             sol += arr[i]
#         else:
#             sol += a
#         if sol > m:
#             return -1
#     return sol
#
#
# n = int(input())
# budget = list(map(int, input().split()))
# m = int(input())
# arr = [0]*n
# maxa = -1
# mid = 0
# res = 0
# start = 0
# end = 1000000000
# # print(arr)
#
# for i in range(n):
#     arr[i] = budget[i]
#     mid += arr[i]
#     res = max(res, arr[i])
#
# if mid <= m:
#     print(res)
# else:
#     while start < end:
#         mid = (start+end)//2
#         z = my_budget(mid)
#         if z == -1:
#             end = mid
#         else:
#             if maxa < z:
#                 maxa = z
#                 res = mid
#             start = mid+1
#     print(res)


'''강사님 코드
N = int(input())
arr = list(map(int, input().split()))
M = int(input())

def check(m):
    # 현재 상한가보다 작으면 현 도시예산으로 더하고 아니면 상한가로 더함
    tot = 0
    for i in range(N):
        if arr[i] <= m:
            tot += arr[i]
        else:
            tot += m
    if tot>M:
        return 0
    else:
        return 1
    # 총액을 초과하면 실패 0 아니면 성공 1

e = max(arr)
s, sol = 0, 0
while s<= e:
    m = (s+e)//2
    if check(m):
        sol = m
        s = m+1
    else:
        e = m-1
print(sol)
'''

''' # 그리디로 구현
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
sol = 0
arr.sort()   # 예산액을 오름차순으로 정렬
sol, tot = 0,0
for i in range(n):
    # 현재 도시의 예산액으로 남은도시에 모두 일괄 배정해보고 가능하면 배정
    if tot + arr[i]*(n-i) <= m:
        tot += arr[i]
    # 아니면 지금까지 배정한 금액을 뺀 잔액으로 남은도시에 일괄 배정한다.
    else:
        sol = (m - tot) // (n-i)
        break

if sol:
    print(sol)
else:
    print(arr[-1])
'''
