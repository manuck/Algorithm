import sys
sys.stdin = open("피자 굽기_input.txt")

t = int(input())

for case in range(1):
    N, M = list(map(int, input().split()))
    a = list(map(int, input().split()))

