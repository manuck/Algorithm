import itertools

a = [1, 2, 3, 4]
# 순열
per1 = list(itertools.permutations(a, 3))
print('순열 : ', end="")
print(per1)
print(len(per1[0]))
print(len(per1))

# 중복순열
per2 = itertools.product(a, repeat=2)
print('중복순열 : ', end="")
print(list(per2))

# 조합
com1 = itertools.combinations(a, 2)
print('조합 : ', end="")
print(list(com1))

# 중복조합
com2 = itertools.combinations_with_replacement(a, 2)
print('중복조합 : ', end="")
print(list(com2))
