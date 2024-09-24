#All Permutations of a String
from itertools import permutations

def string_permutations():
    s = input("Введите строку: ")
    perms = [''.join(p) for p in permutations(s)]
    print("Все перестановки строки:")
    for perm in perms:
        print(perm)
