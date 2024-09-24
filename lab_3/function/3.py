# Solve Puzzle: Chickens and Rabbits Problem
def solve():
    numheads = int(input("Введите количество голов: "))
    numlegs = int(input("Введите количество ног: "))
    
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            print(f"Курицы: {chickens}, Кролики: {rabbits}")
            return
    print("Решение не найдено")


