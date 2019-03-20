import sys
sys.stdin = open("최대성적표_input.txt")

t = int(input())
for case in range(1, t+1):
    n, k = map(int,input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    res = 0
    for i in range(k):
        res += a[i]

    print('#%i %i' % (case, res))
