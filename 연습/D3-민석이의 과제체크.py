import sys
sys.stdin = open("민석이의 과제체크_input.txt")

t = int(input())

for case in range(1, t+1):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    b = list(range(1,n+1))
    # print(a)
    # print(b)
    res = ''
    for i in range(len(b)):
        if b[i] not in a:
            res += str(b[i]) + ' '

    print('#%i %s' %(case, res))