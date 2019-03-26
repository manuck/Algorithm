import sys
sys.stdin = open("B1_input.txt")

# 눈의 중복 순열
def dfs(no, nsum):
    global n, m, arr
    if no > n:
        if nsum == m:
            for i in range(1, n+1):
                print(arr[i], end=" ")
            print()
        return
    for i in range(1, 7):
        arr[no] = i
        dfs(no+1, nsum+i)

# 눈의 중복을 배제한 순열
def dfs2(no):
    global n
    if no > n:
        for i in range(1, n+1):
            print(arr[i], end=" ")
        print()
        return
    for i in range(1, 7):
        if chk[i] == 1: continue
        chk[i] = 1
        arr[no] = i
        dfs2(no+1)
        chk[i] = 0


n, m = map(int, input().split())
# print(n, m)
res = []
arr = [0] * 8
chk = [0] * 7

dfs(1, 0)

# dfs2(1)
# print(res)
# print(res)