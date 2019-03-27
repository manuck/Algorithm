import sys
sys.stdin = open("B6_input.txt")

def DFS(no): # a[no]번째 구슬을 상자에 담거나 담지 않는 모든 경우
    # 1] 리턴조건 : N번째이면 인쇄후 리턴
    global k, flag
    if flag==1: return
    if no >= n:
        sol = 0
        for i in range(n):
            sol += b[i]
            # print(b[i], end=" ")
            if sol > k: return
            if sol == k:
                # print(sol)
                res.append(sol)
                break
        # print()
        if len(res) != 0:
            flag = 1
        return
    # if flag == 1:
    #     return
# 2] 현재 구슬을 고르기(b배열에 담기)
    b[no] = a[no]
    DFS(no + 1)
# 3] 현재 구슬을 고르지 않기(b배열에 담지 않기)
    b[no] = 0
    DFS(no+1)


t = int(input())
for case in range(t):
    n, k = map(int,input().split())
    a = list(map(int, input().split()))
    # print(a)
    b = [0]*n
    flag = 0
    res = []
    DFS(0)
    if res:
        print("YES")
    else:
        print("NO")