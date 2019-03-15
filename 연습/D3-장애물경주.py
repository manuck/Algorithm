import sys
sys.stdin = open("장애물경주_input.txt")

t = int(input())

for case in range(1, t+1):
    n = int(input())
    a = list(map(int, input().split()))
    ol = 0
    na = 0

    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            if na < a[i] - a[i+1]:
                na = a[i] - a[i+1]
        elif a[i] < a[i+1]:
            if ol < a[i+1] - a[i]:
                ol = a[i+1] - a[i]

    print('#%i %i %i' % (case, ol, na))