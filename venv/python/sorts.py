L = (('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88))

# L[0]=('Bob', 100)

# L.sort()

print(list(range(1, 4)))

print(L)


def by_name(t):
    return t[0].lower()


L2 = sorted(filter(lambda t: t[1] > 80, L), key=lambda t: t[0].lower())

print(L2)
