#Fahrenheit to Celsius Conversion
def fahrenheit_to_celsius():
    fahrenheit = float(input("Введите температуру в градусах Фаренгейта: "))
    celsius = (5 / 9) * (fahrenheit - 32)
    print(f"Эквивалентная температура в градусах Цельсия: {celsius:.2f}")
