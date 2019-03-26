import sys
sys.stdin = open("B3_input.txt")

# def process_solution(a, k, sum):
#     global nmin
#     if sum > nmin : return
#
# def make_candidates(a, k, input, c):
#     in_perm = [0] * NMAX
#
#     for i in range(1, k):
#         in_perm[a[i]] = 1
#
#     ncands = 0
#     for i in range(1, input+1):
#         if in_perm[i] == 0:
#             c[ncands] = i
#             ncands += 1
#
#     return ncands
#
# def backtrack(a, k, input, sum):
#     global nmin
#
#     if sum > nmin: return
#
#     global MAXCANDIDATES
#     c = [0] * MAXCANDIDATES
#
#     if k == input:
#         process_solution(a, k, sum)
#         if sum < nmin:
#             nmin = sum
#             sum=0
#     else:
#         k += 1
#         ncands = make_candidates(a, k, input, c)
#         for i in range(ncands):
#             a[k] = c[i]
#             backtrack(a, k, input, sum + arr[k-1][a[k]-1])
#
# n = int(input())
# arr = [[0 for _ in range(n)] for _ in range(n)]
# for i in range(n):
#     arr[i] = list(map(int, input().split()))
#
# MAXCANDIDATES = 100
# NMAX = 100
# data = [0]
# nmin = 99999
# for i in range(n):
#     data.append(i)
# a = [0] * NMAX
# backtrack(a, 0, n, 0)
# # minres = []
# # for i in range(n):
# #     minres.append(min(arr[i]))
# # print(sum(minres))
# print(nmin)



def dfs1(no, nsum):
    global sol
    if nsum > sol : return # 가지치기
    if no >= n:
        # for i in range(n): print(rec[i], end=" ")
        # print(nsum)
        if nsum<sol:
            sol = nsum
        return
    # 현재 행에 모든 열의 수를 고르는 경우의 수 시도
    for i in range(n):
        rec[no] = arr[no][i]
        dfs1(no+1, nsum + arr[no][i])
    # print(sol)

def dfs2(no, nsum):
    global sol
    if nsum > sol : return # 가지치기
    if no >= n:
        # for i in range(n): print(rec[i], end=" ")
        # print(nsum)
        if nsum < sol:
            sol = nsum
        return
    # 현재 행에 모든 열의 수를 고르는 경우의 수 시도
    for i in range(n):
        if chk[i] == 1:continue
        chk[i] = 1
        rec[no] = arr[no][i]
        dfs2(no+1, nsum + arr[no][i])
        chk[i] = 0

n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))

sol = 100000
chk = [0] * 11
rec = [0] * 11

dfs1(0,0)
print(sol)
sol = 100000
dfs2(0,0)
print(sol)