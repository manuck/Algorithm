import sys
sys.stdin = open("건초더미_input.txt")

t = int(input())

for case in range(1, t+1):
    n = int(input())
    a = []
    avg = 0
    for i in range(n):
        b = int(input())
        a.append(b)
        avg += b
    res = 0
    avg = int(avg/len(a))
    for i in range(len(a)):
        if a[i] < avg:
            res += avg - a[i]

    print('#%i %i' % (case, res))

    # print('#%i %i' % (case, cnt))
