def is_palindrome(s):
    """
    Функция проверки строки на палиндром
    """
    return s == s[::-1]  # сравниваем строку с ее перевернутой версией
