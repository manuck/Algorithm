import sys
sys.stdin = open("직사각형_input.txt")


t = int(input())

for case in range(1,t+1):
    a = list(map(int, input().split()))
    res = 0
    for i in range(3):
       if a.count(a[i]) != 2:
           res = a[i]

    print('#%i %i' %(case, res))