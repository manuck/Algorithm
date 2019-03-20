import sys
sys.stdin = open("홀수짝수_input.txt")

t = int(input())
for case in range(1, t+1):
    n = int(input())

    print('#%i' % (case), end=" ")
    if n%2 == 0:
        print('Even')
    else:
        print('Odd')