import sys
sys.stdin = open("사냥꾼_input.txt")

# n = int(input())
# a = [[0 for _ in range(n)]for _ in range(n)]
# for i in range(n):
#     a[i] = list(input())
#     print(a[i])
# print()
# xi = []
# yi = []
#
#
# while True:
#     flag = 0
#     flag2 = 0
#     for i in range(n):
#         for j in range(n):
#             if a[i][j] == '1':
#                 xi.append(j)
#                 yi.append(i)
#                 a[i][j] = '3'
#                 flag = 1
#                 break
#         if flag == 1:
#             break
#     for i in range(n):
#         for j in range(n):
#             if a[i][j] == '1':
#                 flag2 = 0
#             else:
#                 flag2 += 1
#     if flag2 == n*n:
#         break
#
#
# for i in range(n):
#     print(a[i])
# print()
#
#
# for i in range(n):
#     print(a[i])
#
# print(xi)
# print(yi)
#
# dy = [1, 0, -1, 0, 1, -1, 1, -1]
# dx = [0, -1, 0, 1, 1, -1, -1, 1]
#
# dindex = 0
# cnt = 0
# hunti=0
#
# for q in range(len(xi)):
#     for i in range(8):
#         xx = xi[hunti]
#         yy = yi[hunti]
#
#         while True:
#             xx += dx[dindex]
#             yy += dy[dindex]
#
#             if a[yy][xx] == '2':
#                 a[yy][xx] = '0'
#                 cnt += 1
#
#             elif a[yy][xx] == '0' or a[yy][xx] == '3':
#                 dindex += 1
#                 xx = xi[hunti]
#                 yy = yi[hunti]
#                 if dindex == 8:
#                     break
#
#             print(cnt)
#             for j in range(n):
#                 print(a[j])
#         # hunti += 1


def check(r, c): #현재 위치에서 8방향의 토끼 카운트
    cnt = 0
    dr = [-1, 1, 0, 0, -1, 1, -1, 1]
    dc = [0, 0, -1, 1, -1, -1, 1, 1]
    for k in range(8): #8방향
        for dep in range(1, n): # 현위치에서 떨어진 거리
            nr = r + dr[k]*dep
            nc = c + dc[k]*dep
            # 범위를 벗어났거나 0 또는 1 이면 탈출
            if nr < 0 or nr >= n or nc < 0 or nc >= n or arr[nr][nc] < 2:
                break
            elif arr[nr][nc]==2 : #토끼라면 지우고 카운트
                arr[nr][nc] = 3
                cnt += 1
    return cnt

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input())))

sol = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1: # 사냥꿑위치에서 탐색 시작
            sol += check(i, j)
print(sol)
