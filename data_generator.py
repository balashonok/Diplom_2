import random
import string

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def generate_user_data():
    login = generate_random_string(10)
    password = generate_random_string(10)
    name = generate_random_string(10)

    payload = {
        "email": f'{login}@yandex.ru',
        "password": password,
        "name": name
    }

    return payload