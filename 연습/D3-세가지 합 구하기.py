import sys
sys.stdin = open("세가지 합 구하기_input.txt")

def s1sum(n):


t = int(input())
for case in range(1,t+1):
    n = int(input())
    s1, s2, s3 = 0, 0, 0
    for i in range(1, n+1):
        s1 += i
        s2 += 2*i-1
        s3 += 2*i
    print('#%i ' % case, end="")
    print(s1, s2, s3)
