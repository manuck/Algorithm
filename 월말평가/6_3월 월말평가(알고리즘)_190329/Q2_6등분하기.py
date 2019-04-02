import sys
sys.stdin = open("Q2_input.txt")


t = int(input())
for case in range(1, t+1):
    n, m = map(int, input().split())
    a = [[0 for _ in range(n)]for _ in range(m)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
        # print(a[i])
    sol = 0
    for i in range(1, n):
        for j in range(1, m-3):
            for k in range(j+1, m-2):
                for q in range(k+1, m-1):
                    temp = []
                    sec1sum = 0
                    sec2sum = 0
                    sec3sum = 0
                    sec4sum = 0
                    sec5sum = 0
                    sec6sum = 0
                    for sec1i in range(i):
                        for sec1j in range(k):
                            sec1sum += a[sec1i][sec1j]
                    # print(sec1sum)

                    for sec2i in range(i):
                        for sec2j in range(k, q):
                            sec2sum += a[sec2i][sec2j]
                    # print(sec2sum)

                    for sec3i in range(i):
                        for sec3j in range(q, m):
                            sec3sum += a[sec3i][sec3j]
                    # print(sec3sum)

                    for sec4i in range(i, n):
                        for sec4j in range(k):
                            sec4sum += a[sec4i][sec4j]
                    # print(sec4sum)

                    for sec5i in range(i, n):
                        for sec5j in range(k, q):
                            sec5sum += a[sec5i][sec5j]
                    # print(sec5sum)

                    for sec6i in range(i, n):
                        for sec6j in range(q, m):
                            sec6sum += a[sec6i][sec6j]
                    # print(sec6sum)

                    temp.append(sec1sum)
                    temp.append(sec2sum)
                    temp.append(sec3sum)
                    temp.append(sec4sum)
                    temp.append(sec5sum)
                    temp.append(sec6sum)

                    for tempi in range(6):
                        for tempj in range(6):
                            for tempk in range(6):
                                tempsum = 0
                                if tempi != tempj != tempk:
                                    tempsum += abs(temp[tempi] - temp[tempj])
                                    tempsum += abs(temp[tempj] - temp[tempk])
                                    tempsum += abs(temp[tempk] - temp[tempi])
                                    if sol < tempsum:
                                        sol = tempsum
    print('#%i ' % (case) , end="")
    print(sol)