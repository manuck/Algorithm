r = int(input())


x = 0
for i in range(1, r+1):
    for j in range(1, r+1):
        if r*r >= i*i + j*j:
            x += 1
x = x*4
print(x)
