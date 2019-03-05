import sys
sys.stdin = open("소수의 개수와 최대 최소 구하기_input.txt")

a, b = map(int, input().split())
arr = [0]*100001 # 소수는 0, 소수아니면 1로 체크

def aretos(e): #에레토스테네스의 체
    for i in range(2, e+1): # 배수
        if arr[i] :
            continue # 이미 체크됐으면 스킵
        if i*i > e:
            break # 루트값까지만 배수 시도
        for j in range(i*2, e+1, i):
            arr[j] = 1 # 배수값들을 체크

if a > b:
    a, b = b, a

arr[1] = 1
aretos(b)

cnt = 0
for i in range(a, b+1):
    if arr[i] == 0:
        cnt += 1

arrmin = b
arrmax = a
for i in range(a, b):
    if arr[i] == 0:
        if i < arrmin:
            arrmin = i

        if i > arrmax:
            arrmax = i
print(cnt)
print(arrmax+arrmin)
