import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

pass_q = input('How many passwords do you need? Please enter number: ')
passlen = input('Enter password length in numbers. (For example: 5): ')
pass_dig = input('Do you want to add digits to your password? Type y(yes) or n(no): ')
pass_up = input('Do you want to add upperscase letters to your password? Type y(yes) or n(no): ')
pass_low = input('Do you want to add lowercase letters to your password? Type y(yes) or n(no): ')
pass_ambig = input('Do you want to remove ambiguity symbols your password? Type y(yes) or n(no): ')

if pass_dig == 'y':
    chars += digits
if pass_up == 'y':
    chars += uppercase_letters
if pass_low == 'y':
    chars += lowercase_letters
if pass_ambig == 'y':
    for c in 'il1Lo0O':
        chars.replace(c, '')


def generate_password(length, char):
    new_pass = ''
    for _ in range(length):
        new_pass += random.choice(char)
    return new_pass


for _ in range(int(pass_q)):
    print(generate_password(int(passlen), chars))
