import sys
sys.stdin = open("늘어지는 소리 만들기_input.txt")

t = int(input())
for case in range(1, t+1):
    a = list(input())
    n = int(input())
    index = list(map(int, input().split()))
    res = a
    index.sort(reverse=True)

    for i in range(len(index)):
        a.insert(index[i], '-')

    print('#%i'% (case), end=" " )
    for i in range(len(a)):
        print(a[i], end="")

    print()