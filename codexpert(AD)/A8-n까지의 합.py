import sys
sys.stdin = open("A8_input.txt")

def my_sum(a):
    global res, n
    if a > n: return
    res += a
    # print(a)
    my_sum(a+1)

n = int(input())
res = 0
# for i in range(1,n+1):
#     res += i
my_sum(1)
print(res)