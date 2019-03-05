import sys
sys.stdin = open("스파이 조직_input.txt")

n, arr = input().split()

n = int(n)
# print(n)
# print(arr)
dep = 0
i = 0
while i < len(arr):
    if arr[i] == '<':
        dep += 1
    elif arr[i] == '>':
        dep -= 1
    else:
        if dep == n:
            for j in range(i, i+5):
                if arr[j] == '<' or arr[j] == '>':
                    break
                else:
                    print(arr[j], end='')
            i = j-1
            print(end=' ')
    i += 1