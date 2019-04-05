import time
from time import strftime
import sys
sys.stdin = open("(1247)최적경로_input.txt", "r")
T = int(input())
def getD(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def calc():
    global ans
    dist = 0
    for i in range(N-1):
        dist += getD(customer[A[i]], customer[A[i+1]])  # 고객간의 거리
    dist += getD(company, customer[A[0]])               # 회사 - 첫번째 고객
    dist += getD(customer[A[N-1]], home)                # 마지막고객 - 집

    if ans > dist: ans = dist

def perm(n, k):
    if k == n:
        calc()
    else:
        for i in range(k, n, 1):
            A[k], A[i] = A[i], A[k]
            perm(n, k+1)
            A[k], A[i] = A[i], A[k]

for tc in range(T):
    start_time = time.time()

    N = int(input())
    temp = list(map(int, input().split()))
    A = list(range(N))              # 고객의 순열
    ans = 0x7fffffff

    company = (temp[0], temp[1])    # 회사
    home = (temp[2], temp[3])       # 집
    customer = []                   # 고객

    for i in range(4, len(temp), 2):
        customer.append((temp[i], temp[i+1]))

    perm(N, 0)
    print("#{} {}".format(tc+1, ans))

print(time.time() - start_time, 'seconds')