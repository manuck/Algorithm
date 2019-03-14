def comb(n, r):
    if r == 0:
        return 1
    elif n < r:
        return 0
    else:
        # T[r-1] = A[n-1]
        return comb(n-1, r-1) + comb(n-1, r)

print(comb(4, 3))