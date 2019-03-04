import sys
sys.stdin = open("덧셈_input.txt")

num, X = list(map(str, input().split()))
print(len(num))
print(X)

for i in range(len(num)):
    a = 0
    b = 0
    for j in range(i):
        a += int(num[j])

        for q in range(i,len(num)):
            b += int(num[q])
            if a+b== int(X):
                print()


