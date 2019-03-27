data = [1,2,3,4,5,6,7,8,9,10]
A = [0]*10
count = 0
total = 0
def printset(n):
    global count
    sol = 0
    for i in range(n):
        if A[i] == 1:
            sol += data[i]

    if sol == 10:
        count += 1
        print("%d : " % count, end="")
        for j in range(n):
            if A[j] == 1:
                print(data[j], end=" ")
        print()

def powerset(n, k, sum): # n: 원소의 갯수, k: 현재depth
    global total
    if sum > 10: return     # 가지치기
    total += 1
    if n == k:      # basis part
        printset(n)
    else:
        A[k] = 1
        powerset(n, k+1, sum + data[k])
        A[k] = 0
        powerset(n, k+1, sum)

powerset(10, 0, 0)
print(total)