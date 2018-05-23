import getpass


def passwords_mark(password):
    mark = 0
    if len(password) >= 8:
        mark += 2
    if any(word.isupper() for word in password):
        mark += 2
    if any(word.islower() for word in password):
        mark += 2
    if any(word.isdigit() for word in password):
        mark += 2
    if any(["!", "@", "#", "$", "%", "^", "&", "*"] for word in password):
        mark += 2
    return mark


def print_mark(password_strength, password_mark):
    print(password_strength, password_mark)


def get_password():
    password = getpass.getpass("Введите пароль: ")
    return password


if __name__ == "__main__":
    password = get_password()
    password_mark = passwords_mark(password)
    print_mark("Сложность пароля: ", password_mark)
