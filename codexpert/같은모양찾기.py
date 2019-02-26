import sys
sys.stdin = open("같은모양찾기_input.txt")

n = int(input())
a = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    a[i] = list(input())

vs = int(input())
b = [[0 for _ in range(n)] for _ in range(n)]
for i in range(vs):
    b[i] = list(input())

res= 0
for i in range(n-vs+1):
    for j in range(n-vs+1):
        cnt = 0
        for z in range(vs):
            for c in range(vs):
                if a[i+z][j+c] == b[z][c]:
                    cnt += 1
                    # print(cnt)
        if cnt == vs**2:
            res += 1


print(res)