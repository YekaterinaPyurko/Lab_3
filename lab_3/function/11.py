#Check if a Word or Phrase is a Palindrome
def is_palindrome():
    s = input("Введите слово или фразу: ").replace(" ", "").lower()
    if s == s[::-1]:
        print("Это палиндром")
    else:
        print("Это не палиндром")
