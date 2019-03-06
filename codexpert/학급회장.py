import sys
sys.stdin = open("학급회장_input.txt")

n = int(input())

a = [[0 for _ in range(3)]for _ in range(n)]

for i in range(n):
    a[i] = list(map(int, input().split()))

print(a)

score = []
st1=[]
st2=[]
st3=[]
st = []
for i in range(3):
    sc = 0
    for j in range(n):
        sc += a[j][i]
    score.append(sc)

for i in range(n):
    st1.append(a[i][0])
for i in range(n):
    st2.append(a[i][1])
for i in range(n):
    st3.append(a[i][2])
st.append(st1)
st.append(st2)
st.append(st3)
index = []
for i in range(len(score)):
    if max(score) == score[i]:
        index.append(i+1)

print(score)
print(st)
print(index)

points = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for j in range(3):
    for i in range(n):
        if st[j][i] == 3:
            points[j][0]+=1
        elif st[j][i] == 2:
            points[j][1]+=1
        elif st[j][i] == 1:
            points[j][2]+=1
print(points)
dic = {}
for i in range(1,4):
    dic[i]=points[i-1]
print(dic)







