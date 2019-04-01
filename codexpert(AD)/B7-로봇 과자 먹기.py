import sys
sys.stdin = open("B7_input.txt")

# def perm(n, k):
#     global msum
#     if n == k:
#         # print(a)
#         psum = 0
#         for i in range(n):
#             psum += abs(s[2*a[i]]-r[2*i])+abs(s[2*a[i]+1]-r[2*i+1])
#             if psum > msum: return
#         if msum > psum:
#             msum = psum
#     else:
#         for i in range(k, n):
#             a[i], a[k] = a[k], a[i]
#             perm(n, k+1)
#             a[i], a[k] = a[k], a[i]
#
#
# t = int(input())
# for case in range(1, t+1):
#     n = int(input())
#     s = list(map(int, input().split()))
#     r = list(map(int, input().split()))
#     msum = 9999999999
#
#     a = list(range(n))
#
#     perm(n, 0)
#     print(msum)

def DFS(no, nsum):  # 현재 로봇(행)에서 모든 과자를 먹는 경우의 수
    global nmin
    if nsum > nmin:return # 가지치기
    if no >= n:
        if nsum<nmin : nmin = nsum
        return
    for i in range(n):  # 과자 (열)
        if chk[i] : continue
        chk[i] = 1
        DFS(no+1, nsum+arr[no][i])
        chk[i] = 0

t = int(input())
for case in range(t):
    n = int(input())
    snack = list(map(int, input().split()))
    robot = list(map(int, input().split()))
    ads = 0
    chk = [0]*n
    arr = [[0]*n for _ in range(n)]
    nmin = 99999
    for i in range(n):
        for j in range(n):
            dist = abs(robot[i*2] - snack[j*2]) + abs(robot[i*2+1] - snack[j*2+1])
            arr[i][j] = dist
    # print(arr)
    DFS(0,0)
    print(nmin)

