import sys
sys.stdin = open("0117_input.txt")


def maxmin(li):
    maxN = 0
    minN = 9999
    maxid = 0
    minid = 0
    for i in range(len(li)):
        if maxN < li[i]:
            maxN = li[i]
            maxid = i
        if minN > li[i]:
            minN = li[i]
            minid = i
    return maxN, minN ,maxid, minid

for i in range(10):
    n = input()
    num = list(map(int, input().split()))
    maxN, minN, maxid, minid = maxmin(num)
    for j in range(int(n)):
        maxN -= 1
        minN += 1
        num[maxid] -= 1
        num[minid] += 1
        maxN, minN, maxid, minid = maxmin(num)
    print(f'#{i+1} {maxN-minN}')
