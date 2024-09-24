#Print Histogram from a List of Integers
def histogram():
    lst = list(map(int, input("Введите список чисел, разделенных пробелом: ").split()))
    for n in lst:
        print('*' * n)
