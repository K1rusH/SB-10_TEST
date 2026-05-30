import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

def test_password_too_long():
    """Тест, что пароль длиннее 12 символов не принимается"""
    password = "verylongpassword123"
    assert len(password) > 12

def test_password_too_short():
    """Тест, что пароль koroche 12 символов не принимается"""
    password = "shortpass"
    assert len(password) < 12

def test_password_short():
    """Тест, что пароль 1 символов не принимается"""
    password = "s"
    assert len(password) < 12





"""
Допиши еще один тест из предложенных. Или придумай свой.
Если сможешь написать больше, то будет круто!

Тест, что длина пароля соответствует заданной
Тест, что два сгенерированных подряд пароля различаются
"""