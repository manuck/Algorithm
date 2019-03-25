import sys
sys.stdin = open("안경이없어_input.txt")

t = int(input())

for case in range(1, t+1):
    a, b = list(map(str, input().split()))

    acnt = 0
    bcnt = 0

    for i in a:
        if i == 'A' or i == 'D' or i == 'O' or i == 'P' or i == 'Q' or i == 'R':
            acnt += 1
        elif i == 'B':
            acnt += 2

    for i in b:
        if i == 'A' or i == 'D' or i == 'O' or i == 'P' or i == 'Q' or i == 'R':
            bcnt += 1
        elif i == 'B':
            bcnt += 2

    print('#%i'%(case), end=" ")
    if acnt == bcnt:
        print('SAME')
    else:
        print('DIFF')