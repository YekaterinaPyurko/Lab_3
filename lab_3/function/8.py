#Check if List Contains 007 in Order
def spy_game():
    nums = list(map(int, input("Введите список чисел, разделенных пробелом: ").split()))
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            print("True")
            return
    print("False")
