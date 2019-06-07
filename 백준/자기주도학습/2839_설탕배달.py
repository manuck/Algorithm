n = int(input())

# 5kg 봉지, 3kg 봉지

big = n // 5
q = n % 5
small = 0

if q == 1:
    big -= 1
    small = 2
elif q == 2:
    big -= 2
    small = 4
elif q == 3:
    small = 1
elif q == 4:
    big -= 1
    small = 3

if big < 0 or small < 0:
    print( -1 )
else:
    print( big + small )