import sys
sys.stdin = open("모음이보이지않는사람_input.txt")

t = int(input())

for case in range(1, t+1):
    a = list(input())
    mo = ['a', 'e', 'i', 'o', 'u']
    res = ''
    for i in range(len(a)):
        if a[i] not in mo:
            res += a[i]

    print('#%i %s' % (case, res))
