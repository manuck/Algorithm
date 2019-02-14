import sys
sys.stdin = open("종이붙이기_input.txt")

# DP 적용
# def dfs(n):
#     f = [1, 3]
#     for i in range(2, n+1):
#         f.append(f[i-1] + 2*f[i-2])
#
#     return f[n-1]

# 재귀
def dfs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return dfs(n-1) + 2*dfs(n-2)

T = int(input())
for case in range(1, T + 1):
    N = int(input())
    N =int(N/10)
    res = dfs(N)
    print(f'#{case} {res}')