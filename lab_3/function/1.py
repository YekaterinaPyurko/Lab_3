#Grams to Ounces Conversion
def grams_to_ounces():
    grams = float(input("Введите количество граммов: "))
    ounces = grams * 0.03527396
    print(f"{grams} граммов = {ounces:.2f} унций")
