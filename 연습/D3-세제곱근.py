import sys
sys.stdin = open("세제곱근_input.txt")

t = int(input())
for case in range(1,t+1):
    n = int(input())
    a = n
    b = 1
    while b**3 < a:
        if b**3 == a:
            break
        else:
            b+=1
    print('#%i' %(case), end=" ")
    if b**3 > a:
        print(-1)
    else:
        print(b)