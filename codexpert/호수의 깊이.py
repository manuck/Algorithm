import sys
sys.stdin = open("호수의 깊이_input.txt")

n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

# print(a)

for case in range(4):

    for i in range(n):
        cnt = 0
        for j in range(n):
            if a[i][j] == 0:
                cnt = 0
            if a[i][j] >= 1:
                cnt += 1
                a[i][j] = cnt

    for i in range(n):
        cnt = 0
        for j in range(n):
            if a[j][i] == 0:
                cnt = 0
            if a[j][i] >= 1:
                cnt += 1
                if a[j][i] > cnt:
                    a[j][i] = cnt

    for i in range(n):
        cnt = 0
        for j in range(n):
            if a[i][~j] == 0:
                cnt = 0

            if a[i][~j] >= 1:
                cnt += 1
                if a[i][~j] > cnt:
                    a[i][~j] = cnt

    for i in range(n):
        cnt = 0
        for j in range(n):
            if a[~j][i] == 0:
                cnt = 0
            if a[~j][i] >= 1:
                cnt += 1
                if a[~j][i] > cnt:
                    a[~j][i] = cnt


# for i in range(n):
#     print(a[i])
res = 0
for i in range(n):
    for j in range(n):
        res += a[i][j]
print(res)

## 강사님 코드

# def check(si, sj):
#     dr = [-1, 1, 0, 0]
#     dc = [0, 0, -1, 1]
#     # 4방향중 짧은 거리를 리턴
#     for dep in range(1, n): # 깊이
#         for k in range(4): # 4방향
#             if a[ si+dr[k]*dep ][ sj+dc[k]*dep ] == 0:
#                 return dep
#
# sol = 0
# for i in range(n):
#     for j in range(n):
#         if a[i][j] == 1:
#             sol += check(i,j)
# print(sol)