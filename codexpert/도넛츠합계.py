import sys
sys.stdin = open("도넛츠합계_input.txt")

# N = 맵의 크기, K = 도너츠 크기
N, K = map(int, input().split())
a = [[0 for _ in range(N)]for _ in range(N)]

for i in range(N):
    a[i] = list(map(int, input().split()))

# print(a)
sumres = 0
for i in range(N-K+1):
    for j in range(N-K+1):
        sum1 = 0

        for y in range(K):
            for x in range(K):
                if y == 1 and x == 1:
                    # print(a[i+y][j+x])
                    pass
                else:
                    sum1 += a[i+y][j+x]

        if sumres < sum1:
            sumres = sum1

print(sumres)
