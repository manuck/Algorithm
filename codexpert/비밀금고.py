import sys
sys.stdin = open("비밀금고_input.txt")

n = int(input())
a = [[0 for _ in range(n+2)]for _ in range(n+2)]
print(a)
num = list(map(int, input().split()))

print(num)

