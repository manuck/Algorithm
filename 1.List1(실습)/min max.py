import sys
sys.stdin = open("minmax_input.txt")


n = input()
result = 0

for i in range(int(n)):
    a = input()
    numbers = list(map(int,input().split()))

    for j in range(len(numbers)-1,0,-1):
        for k in range(0,j):
            if numbers[k] > numbers[k+1]:
                numbers[k],numbers[k+1] = numbers[k+1],numbers[k]

    result = numbers[~0] - numbers[0]
    print(f'#{i+1} {result}')