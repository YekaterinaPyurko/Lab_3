#Filter Prime Numbers from a List
def filter_prime():
    numbers = list(map(int, input("Введите числа, разделенные пробелом: ").split()))
    
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    primes = [num for num in numbers if is_prime(num)]
    print(f"Простые числа: {primes}")
