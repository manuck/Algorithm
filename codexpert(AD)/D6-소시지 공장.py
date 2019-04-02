import sys, time
sys.stdin = open("D6_input.txt")

n = int(input())
a = list(map(int,input().split()))
# print(a)
b = [0]*n
for i in range(n):
    b[i] = [a[i*2], a[i*2+1]]

visit = [0]*n
# print(b)
b.sort()
b.sort()
# print(b)
cnt = 0
index = 0
asd = 0
while True:
    asd += 1
    for i in range(index+1, n):
        if b[index][0] <= b[i][0] and b[index][1] <= b[i][1]:
            # print(b[i])
            cnt += 1
            index = i
            break

    if asd == n:
        cnt+=1
        break
# print(cnt)
# start_time = time.time()
# for i in range(n):
#     for j in range(i+1, n):
#         if visit[j] != 1:
#             if b[i][0] <= b[j][0] and b[i][1] <= b[j][1]:
#                 visit[j] = 1
#                 cnt += 1
            # break
# print("---{}s seconds---".format(time.time()-start_time))
print(n-cnt)