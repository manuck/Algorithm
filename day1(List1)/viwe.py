import sys
sys.stdin = open("view_input.txt")
T = 10
for tc in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = 0
    for i in range(len(numbers)-2):
        if numbers[i] > numbers[i + 1] and numbers[i] > numbers[i + 2] and numbers[i] > numbers[i - 1] and numbers[i] > \
                numbers[i - 2]:
            if numbers[i + 1] >= numbers[i + 2] and numbers[i + 1] >= numbers[i - 1] and numbers[i + 1] >= numbers[
                i - 2]:
                result += numbers[i] - numbers[i + 1]
            elif numbers[i + 2] >= numbers[i + 1] and numbers[i + 2] >= numbers[i - 1] and numbers[i + 2] >= numbers[
                i - 2]:
                result += numbers[i] - numbers[i + 2]
            elif numbers[i - 1] >= numbers[i + 2] and numbers[i - 1] >= numbers[i + 1] and numbers[i - 1] >= numbers[
                i - 2]:
                result += numbers[i] - numbers[i - 1]
            elif numbers[i - 2] >= numbers[i + 2] and numbers[i - 2] >= numbers[i + 1] and numbers[i - 2] >= numbers[
                i - 1]:
                result += numbers[i] - numbers[i - 2]
    print(f'#{tc+1} {result}')
    #         print(numbers[i])