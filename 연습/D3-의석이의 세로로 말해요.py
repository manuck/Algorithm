import sys
sys.stdin = open("의석이의 세로로 말해요_input.txt")

t = int(input())
for case in range(1, t+1):
    a = []
    for i in range(5):
        a.append(list(input()))

    n = 0
    for i in range(5):
        if len(a[i])>n:
            n = len(a[i])

    for i in range(5):
        if len(a[i])<n:
            while len(a[i])!= n:
                a[i].append('*')

    print('#%i' % (case), end=" ")
    for i in range(n):
        for j in range(5):
            if a[j][i]!='*':
                print(a[j][i], end="")
    print()