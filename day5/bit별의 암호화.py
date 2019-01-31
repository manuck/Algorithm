def Bbit_print(a): # 이진수
    for i in range(7,-1,-1):
        if a & (1<<i):
            print(1, end="")
        else:
            print(0, end="")
    print()

a = 0x86 # 1000 0110
key = 0xAA # 1010 1010
print("a      ==>", end=" ")
Bbit_print(a)
# ^= : exclusive-or (배타적 논리합)
print("a^=key ==>", end=" ")
a ^= key
Bbit_print(a)

print("a^=key ==>", end=" ")
a ^= key
Bbit_print(a)