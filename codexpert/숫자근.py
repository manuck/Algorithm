import sys
sys.stdin = open("숫자근_input.txt")


def root_calc(num):
    while True:
        tot = 0
        while num:
            tot += num % 10  # 일의자리를 분리하면서 누적
            num//=10
        if tot < 10:  # 한자리수면 리턴
            return tot
        num = tot # 한자리수가 아니면 num 갱신하고 다시 시작


def root_calc2(num): # 숫자근을 list 함수를 이용하여
    while True:
        tot=0
        arrNum=list(map(int, str(num)))
        tot = sum(arrNum)

        if tot < 10:
            return  tot
        num = tot

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

rootMax=0
sol = 0

for i in range(n):
    root = root_calc2(arr[i]) # 숫자근 구하는 함수
    # 가장 큰 숫자근이면 큰 숫자근 갱신하고 해당 정수를 솔루션으로
    if rootMax < root:
        rootMax = root
        sol = arr[i]
    # 가장 큰 숫자근과 같은 숫자근이면 더 작은 점수를 솔루션으로
    if rootMax == root:
        if sol > arr[i]:
            sol = arr[i]

print(sol)