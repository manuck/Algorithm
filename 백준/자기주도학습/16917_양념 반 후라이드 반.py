a, b, c, x, y = map(int,input().split())

sol = 0

if (a+b)/2 > c:
    if x>y:
        sol += y*c*2
        sol += (x-y)*a
    elif x<y:
        sol += x * c * 2
        sol += (y - x) * b
    else:
        sol += x*c

else:
    sol += (x*a)+(y*b)

if x < y and y*c*2 < sol:
    sol = y*c*2
elif y < x and x*c*2 < sol:
    sol = x*c*2


print(sol)