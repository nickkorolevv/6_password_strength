import getpass
from string import punctuation


def get_passwords_rating(password, password_rating, min_password_len):
    if any(char in punctuation for char in password):
        password_rating += 1
    if len(password) >= min_password_len:
        password_rating += 2
    if any(char.isupper() for char in password):
        password_rating += 2
    if any(char.islower() for char in password):
        password_rating += 2
    if any(char.isdigit() for char in password):
        password_rating += 2
    if password.lower() != "password":
        password_rating += 1
    return password_rating


def print_pass_strength(password_strength, password_rating):
    print(password_strength, password_rating)


def get_password():
    password = getpass.getpass("Введите пароль: ")
    return password


if __name__ == "__main__":
    password_rating = 0
    min_password_len = 8
    password = get_password()
    password_rating = get_passwords_rating(password, password_rating, min_password_len)
    print_pass_strength("Сложность пароля: ", password_rating)
