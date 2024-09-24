#Check if List Contains 3 Next to a 3
def has_33():
    nums = list(map(int, input("Введите список чисел, разделенных пробелом: ").split()))
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            print("True")
            return
    print("False")
