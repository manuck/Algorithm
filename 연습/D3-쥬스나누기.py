import sys
sys.stdin = open("쥬스나누기_input.txt")


t = int(input())
for case in range(1, t+1):
    n = int(input())

    print('#', end="")
    print(case, end=" ")
    for i in range(1, n+1):
        print('1/', end="")
        print(n, end=" ")

    print()
