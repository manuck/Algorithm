import sys
sys.stdin = open("부분집합의 합_input.txt")

a = [1,2,3,4,5,6,7,8,9,10,11,12]
n = len(a)

t = int(input())
for k in range(t):
    N,K = list(map(int, input().split()))
    cnt = 0
    for i in range(1 << n):
        result=[]
        for j in range(n):
            if i & (1 << j):
                result.append(a[j])
        if len(result) == N and sum(result)== K:
            cnt += 1
    print(f'#{k+1} {cnt}')