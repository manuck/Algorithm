import sys
sys.stdin = open("Prefix_input.txt")

n = input()
for i in range(int(n)):
    max = 0
    min = 999999
    N, M = map(int, input().split())
    numbers = list(map(int,input().split()))
    for j in range(N-M+1):
        sum = 0
        for k in range(j, j+M):
            sum += numbers[k]
        if sum > max:
            max = sum
        if sum < min:
            min = sum

    print(f'#{i+1} {max-min}')
