num = "012345"
C = [0] * 12
# inData = "000111"
# num = int(inData)
# for i in range(len(inData):
#     C[num % 10] += 1
#     num = num // 10 # num //= 10

for i in range(6):
    C[int(num[i])] += 1

i = 0
tri = 0
run = 0
while i < 10:
    if C[i] >= 3:
        C[i] -= 3
        tri += 1
        continue
    if  C[i] >= 1 and C[i+1] >=1 and C[i+2]>=1:
        C[i] -= 1
        C[i+1] -= 1
        C[i+2] -= 1
        run += 1
        continue
    i += 1
if tri+run == 2:
    print('Baby Gin')
else:
    print('Not')