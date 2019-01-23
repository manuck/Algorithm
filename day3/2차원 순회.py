a = [[0,1,2,3],
     [4,5,6,7],
     [8,9,10,11]]


#행우선
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
print()

#열우선
for j in range(len(a[0])):
    for i in range(len(a)):
        print(a[i][j], end=' ')
    print()
print()

#지그재그순회
n = len(a)
m = len(a[0])
for i in range(len(a)):
    for j in range(len(a[0])):
        print(a[i][j + (m-1-2*j)*(i%2)], end=' ')
    print()