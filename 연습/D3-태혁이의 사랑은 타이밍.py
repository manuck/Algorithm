import sys
sys.stdin = open("태혁이의 사랑은 타이밍_input.txt")

t = int(input())

for case in range(1,t+1):
    d, h, m = map(int, input().split())

    res = 0
    dres = (d-11)*24*60
    hres = (h-11)*60
    mres = (m-11)

    res = dres + hres + mres

    if res >= 0:
        print('#%i %i' %(case,res))
    else:
        print('#%i %i' % (case, -1))
