import sys
sys.stdin = open("표준 입출력_input.txt")

n = int(input())
a, b = map(int, input().split())
res = [list(map(int,input())) for _ in range(a)]

print(n)
print(a, b)
for i in range(a):
    for j in range(b):
        print(res[i][j], end="")
    print()
