def ten_other(number, system):
    new_number = []

    while number >= system:
        new_number.append(number % system)

        number //= system

    new_number.append(number)

    if system == 16:

        for i in new_number:

            num_letters = {

                10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'

            }

            if i >= 10:
                new_number[new_number.index(i)] = num_letters[i]

    print(*new_number[::-1], sep='')


def bukva_valid(bukva):
    if not bukva.isalpha():
        print('Нужно ввести букву!')
        return False
    if bukva.isalpha():
        return bukva
    elif bukva in guessed_letters:
        print('Данная буква уже использована, введите другую.')
        return False


def slovo_valid(slovo):
    if not slovo.isalpha():
        print('Нужно ввести слово, состоящее только из букв!')
        return False
    if slovo.isalpha():
        return slovo
    elif slovo in guessed_words:
        print('Данное слово уже использована, введите другую.')
        return False


guessed_letters = []  # список уже названных букв
guessed_words = []

let_word = input('Хотите ввести слово(с) или букву(б)? Введите соответсвующий символ из скобок --> "с" или "б": ')
if let_word == 'б':
    bukva = input('Введите желаемую букву: ')
    guessed_letters += bukva
if let_word == 'c':
    slovo = input('Введите желаемое слово: ')
    guessed_words += slovo
