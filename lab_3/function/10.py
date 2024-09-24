#Return Unique Elements in a List (Without Using Set)
def unique_elements():
    lst = list(map(int, input("Введите список чисел, разделенных пробелом: ").split()))
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    print(f"Уникальные элементы: {unique_list}")
