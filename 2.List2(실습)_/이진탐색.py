import sys
sys.stdin = open("이진탐색_input.txt")

def binarySearch(P, key):
    start = 1
    end = P
    cnt = 0
    while start <= end:
        middle = (start + end) // 2
        if key == middle:
            return cnt
        elif key < middle:
            end = middle
            cnt += 1
        else:
            start = middle
            cnt += 1
    return cnt

t = int(input())
for k in range(t):

    P,A,B = list(map(int, input().split()))

    ca = binarySearch(P, A)
    cb = binarySearch(P, B)

    if ca > cb:
        print(f'#{k+1} B')
    elif cb > ca:
        print(f'#{k+1} A')
    else:
        print(f'#{k+1} 0')