import string
import secrets
import os


def gen(app):
    password = ''.join((secrets.choice(
        string.ascii_letters + string.digits + string.punctuation) for i in range(14)))
    file_path = 'credentials.txt'
    with open('credentials.txt', 'a+') as f:
        if os.stat(file_path).st_size == 0:
            f.write(app + '\n' + password)
        else:
            f.write('\n\n' + app + '\n' + password)
