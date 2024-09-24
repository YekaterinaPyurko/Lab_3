#Calculate Volume of a Sphere
def sphere_volume():
    radius = float(input("Введите радиус сферы: "))
    volume = (4 / 3) * 3.14159265359 * (radius ** 3)
    print(f"Объем сферы: {volume:.2f}")
