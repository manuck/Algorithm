import sys
sys.stdin = open("B8_input.txt")

# def perm(n, k):
#     global cnt
#     if n == k:
#         arr = [[0 for _ in range(n)] for _ in range(n)]
#         for i in range(n):
#             arr[i][a[i]] = 1
#         for i in range(n):
#             c = check(i, a[i])
#             if c == 0:
#                 return
#             else:
#                 print(arr)
#                 cnt+=1
#         for i in range(n):
#             print(arr[i])
#         print()
#     else:
#         for i in range(k, n):
#             a[i], a[k] = a[k], a[i]
#             perm(n, k+1)
#             a[i], a[k] = a[k], a[i]

def dfs(no):    # 현재행(no)에서 모든 열에 퀸을 놓아보는 경우의 수
    global sol
    if no >= n:
        sol += 1
        return
    for i in range(n):  # 열
        if chk1[i]:continue # 세로방향체크
        if chk2[no+i]:continue  # 우방향 대각선 체크
        if chk3[(n-1)-(no-i)]:continue  # 좌방향 대각선 체크
        chk1[i] = chk2[no + i] = chk3[(n - 1) - (no - i)] = 1   # 퀸 놓기
        dfs(no+1)
        chk1[i] = chk2[no + i] = chk3[(n - 1) - (no - i)] = 0   # 퀸 빼기

n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]
chk1 = [0] * n      # 세로열
chk2 = [0] * n * 2  # 우대각
chk3 = [0] * n * 2  # 좌대각
sol = 0
dfs(0)
print(sol)

# def check(r, c):
#     dc = [-1, 0, 1]
#     dr = [-1, -1, -1]
#     for i in range(3):  # 3 방향
#         for k in range(1, n):   # 1배, 2배, .... 떨어진 거리
#             nr = r + dr[i] * k
#             nc = c + dc[i] * k
#             if nr < 0 or nr >= n or nc < 0 or nc >= n: # 범위 벗어나면 탈출
#                 break
#             if arr[nr][nc] == 1:
#                 return 0
#     return 1


