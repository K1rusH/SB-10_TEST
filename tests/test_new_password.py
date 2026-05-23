import string
from password.new_password import generate_password

def test_password_characters():
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)
    for char in password:
        assert char in valid_characters

def test_password_length():
    for length in [0, 1, 5, 8, 12, 15, 20, 50, 100]:
        password = generate_password(length)
        assert len(password) == length

def test_passwords_are_different():
    password1 = generate_password(20)
    password2 = generate_password(20)
    assert password1 != password2
    
    passwords = [generate_password(10) for _ in range(5)]
    assert len(set(passwords)) == len(passwords)

def test_password_not_empty():
    password = generate_password(10)
    assert len(password) > 0
    assert password != ""

def test_password_contains_all_character_types():
    password = generate_password(30)
    has_letters = any(c.isalpha() for c in password)
    has_digits = any(c.isdigit() for c in password)
    has_punctuation = any(c in string.punctuation for c in password)
    assert has_letters and has_digits and has_punctuation

def test_special_cases():
    password_zero = generate_password(0)
    assert password_zero == ""
    assert len(password_zero) == 0
    
    password_negative = generate_password(-5)
    assert len(password_negative) >= 0
    
    password_default = generate_password()
    assert len(password_default) == 12

if __name__ == "__main__":
    test_password_characters()
    test_password_length()
    test_passwords_are_different()
    test_password_not_empty()
    test_password_contains_all_character_types()
    test_special_cases()