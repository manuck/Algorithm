import sys
sys.stdin = open("C4_input.txt")

def dfs(no, start):
    if no > n:
        print(rec[no],end=" ")
        return

    for i in range(start, 7):
        rec[no]= i
        dfs(no+1, i+1)


# for i in range(1,7):
#     for j in range(i, 7):
#         for k in range(j, 7):
#             print(i, j, k)

# def myprint(q):
#     while q != 0:
#         q = q-1
#         print(" %d " %(T[q]), end="")
#
#     print()

# def H(n, r, q):
#     if r == 0:
#         print(T[0:3])
#     elif n == 0:
#         return
#     else:
#         T[r-1] = A[n-1]
#         H(n, r-1, q)
#         H(n-1, r, q)
#
#
# A = [1, 2, 3, 4, 5, 6]
# T = [0] * 6
#
# H(6, 3, 3)

n, m = map(int, input().split())
print(n, m)
rec = [0] * 6
dfs(0,1)