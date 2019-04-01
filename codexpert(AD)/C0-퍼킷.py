import sys
sys.stdin = open("B7_input.txt")

def powerset(n, k): # n: 원소의 갯수, k: 현재depth
    global resS, resB
    if n == k:      # basis part
        solb = 0
        sols = 1
        for i in range(n):
            if S[i] == 1:
                solb += b[i]
                sols *= s[i]
        resB.append(solb)
        resS.append(sols)
    else:
        S[k] = 1
        powerset(n, k+1)
        S[k] = 0
        powerset(n, k+1)

n = int(input())
s = []
b = []
S = [0]*n
resS = []
resB = []
for i in range(n):
    sn, sb = map(int, input().split())
    s.append(sn)
    b.append(sb)

# print(s)
# print(b)
# print()
powerset(n, 0)
# print(resS)
# print(resB)
sol = 99999999999999999999999
for i in range(len(resB)-1):
    if sol > abs(resS[i]-resB[i]):
        sol = abs(resS[i]-resB[i])

print(sol)