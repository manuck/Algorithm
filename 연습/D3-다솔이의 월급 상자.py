import sys
sys.stdin = open("다솔이의 월급 상자_input.txt")

t = int(input())
for case in range(1,t+1):
    n = int(input())
    res = 0
    for i in range(n):
        p, x = map(float, input().split())
        res += (p*x)

    print('#%i' % (case), end=" ")
    print('%0.6f' % (res))