from itertools import permutations

def string_permutations(s):
    perms = [''.join(p) for p in permutations(s)]
    return perms


print(string_permutations("abc"))
