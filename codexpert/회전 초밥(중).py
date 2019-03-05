import sys
sys.stdin = open("회전 초밥(중)_input.txt")

# N = 접시수, d = 초밥 가지수, k = 연속접시수, c = 쿠본번호
N, d, k, c = map(int, input().split())
a = []
for i in range(N):
    a.append(input())
print(a)
# 순환을 적용시키기 위해 연속접시-1 만큼 앞에서 리스트 추가
for i in range(k-1):
    a.append(a[i])
print(a)
res = 0
for i in range(len(a)-k):

    # 초밥 종류
    kinds = [0] * (d+1)

    # 접시의 초밥 체크
    for j in range(k):
        kinds[int(a[i+j])] = 1

    # 쿠폰 사용
    kinds[c] = 1

    if res < sum(kinds):
        res = sum(kinds)

print(res)
