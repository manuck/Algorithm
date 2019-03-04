r = int(input())


x = 0
for i in range(1, r+1):
    x += ((r*r)-(i*i))**0.5

print(x)
