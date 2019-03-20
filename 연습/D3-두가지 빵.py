import sys
sys.stdin = open("두가지 빵_input.txt")

t = int(input())

for case in range(1, t+1):
    a, b, c = map(int, input().split())
    # print(a, b, c)
    res = 0
    if a > b:
        res = c//b
    else:
        res = c//a
    print('#%i %i' % (case, res))
