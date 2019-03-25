import sys
sys.stdin = open("A3_input.txt")


def lowerSearch(s, e, data):    # 왼쪽 하한치 위치 탐색
    sol = -1
    while s <= e:
        m = (s+e)//2
        # 데이터를 찾으면 왼쪽영역 재탐색
        if data == arr[m]:
            e = m-1
            sol = m     # 찾은 위치가 현재 왼쪽 경계치 이므로 백업
        # mid보다 데이터가 크면 오른쪽영역 탐색
        elif data > arr[m]:
            s = m + 1
        # mid보다 데이터가 작으면 왼쪽영역 탐색
        else:
            e = m - 1
    return sol

def upperSearch(s, e, data):    # 오른쪽 상한치 위치 탐색
    sol = -1
    while s <= e:
        m = (s+e)//2
        # 데이터를 찾으면 오른영역 재탐색
        if data == arr[m]:
            s = m + 1
            sol = m     # 찾은 위치가 현재 오른쪽 경계치 이므로 백업
        # mid보다 데이터가 크면 오른쪽영역 탐색
        elif data > arr[m]:
            s = m + 1
        # mid보다 데이터가 작으면 왼쪽영역 탐색
        else:
            e = m - 1
    return sol

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

for i in range(m):
    lo = lowerSearch(0, n-1, find[i])
    if lo >= 0:
        up = upperSearch(0, n-1, find[i])
        print(up-lo+1, end=" ")
    else:
        print(0, end=" ")