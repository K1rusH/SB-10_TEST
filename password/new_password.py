import random
import string

def generate_password(length=12):
    """Генерация случайного пароля заданной длины."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(length):
        password += random.choice(characters)
    return password
def test_different_passwords():
    password1 = generate_password()
    password2 = generate_password()
    assert password1 != password2


# Пример использования
password_length = 12  # Вы можете выбрать любую длину пароля
print("Ваш новый пароль:", generate_password(password_length))
