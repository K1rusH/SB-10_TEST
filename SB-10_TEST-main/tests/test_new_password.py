import string
from password.new_password import *

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

def test_proverka1():
    test_lengths = [1, 5, 8, 10, 16, 20, 32, 50, 100]
    
    for length in test_lengths:
        password = generate_password(length)
        assert len(password) == length, f"Для длины {length} получен пароль длиной {len(password)}"

def test_pproverka2():
    password1 = generate_password(20)
    password2 = generate_password(20)
    
    assert password1 != password2, f"Ошибка: пароли одинаковые"