import sys
sys.stdin = open("거듭제곱_input.txt")

for case in range(1,11):
    t = int(input())
    n, m = list(map(int, input().split()))

    res = n**m
    print('#%i %i' % (case, res))