import sys
sys.stdin = open("보충학습과 평균_input.txt")

n = int(input())
for case in range(1, n+1):
    a = list(map(int, input().split()))

    for i in range(len(a)):
        if a[i] < 40:
            a[i]=40

    print('#', end="")
    print(case, end=" ")
    print(int(sum(a)/len(a)))