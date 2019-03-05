import sys
sys.stdin = open("덧셈_input.txt")

num, X = list(map(str, input().split()))

flag = 1
for i in range(1, len(num)):
    sa = num[:i]
    sb = num[i:]

    if int(sa) + int(sb) == int(X):
        print(int(sa), end='+')
        print(int(sb), end='=')
        print(X)
        flag=0
        break
if flag == 1:
    print('NONE')

'''
data = list(map(str, input().split()))
L=len(data[0])
flag=1

for i in range(1, L):
   SA = data[0][:i]
   SB = data[0][i:]
   if int(SA) + int(SB) == int(data[1]):
       print(int(SA), end='+')
       print(int(SB), end='=')
       print(data[1])
       flag=0
       break

if flag==1:
   print('NONE')
'''

