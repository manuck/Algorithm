def process_solution(a, k):
    global cnt
    for i in range(1, k+1):
        print(data[a[i]], end=" ")
    print()
    cnt += 1

def make_candidates(a, k, input, c):
    in_perm = [False] * NMAX

    for i in range(1, k):
        in_perm[a[i]] = True

    ncands = 0
    for i in range(1, input+1):
        if in_perm[i] == False:
            c[ncands] = i
            ncands += 1

    return ncands


def backtrack(a, k, input):
    global MAXCANDIDATES, total_cnt
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k)
    else:
        k += 1
        ncands = make_candidates(a, k, input, c)
        for i in range(ncands):
            a[k] = c[i]
            backtrack(a, k, input)
    total_cnt += 1

MAXCANDIDATES = 100
NMAX = 100
data = [0, 0, 1, 2]
a = [0] * NMAX
cnt = 0
total_cnt = 0
backtrack(a, 0, 3)
print()
print(cnt)
print(total_cnt)