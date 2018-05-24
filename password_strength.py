import getpass
import string


def get_passwords_rating(password, pass_rating):
    password_rating = pass_rating
    min_password_len = 8
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


def check_punctuation(password):
    password_rating = 0
    for char in password:
        if char in list(string.punctuation):
            password_rating += 1
            if password_rating == 1:
                break
    return password_rating


def print_pass_strength(password_strength, password_rating):
    print(password_strength, password_rating)


def get_password():
    password = getpass.getpass("Введите пароль: ")
    return password


if __name__ == "__main__":
    password = get_password()
    pass_rating = check_punctuation(password)
    password_rating = get_passwords_rating(password, pass_rating)
    print_pass_strength("Сложность пароля: ", password_rating)
