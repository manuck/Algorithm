import sys
sys.stdin = open("A2_input.txt")

def binSearch(s, e, data):
    while s<=e:
        m = (s+e)//2
        # min번째값이 찾을 테이터이면 찾은위치 +1 를 리턴
        if data == narr[m]: return  m+1
        # mid번째값 보다 데이타가 크면 오른쪽 영역탐색
        elif data > narr[m] : s = m+1
        # mid번째 값 보다 데이터가 작으면 왼쪾 영역 탐색
        else : e = m-1
    # 못찾으면 0 리턴
    return 0
n = int(input())
narr = list(map(int, input().split()))
t = int(input())
find = list(map(int, input().split()))

for i in range(t):
    sol = binSearch(0, n-1, find[i])
    if sol == -1: print(0)
    else: print(sol)





# for i in range(t):
#     for j in range(n):
#         if data[j] == find[i]:
#             print(j+1)
#             break
#     if find[i] not in data:
#         print('0')