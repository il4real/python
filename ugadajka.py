from random import randint

a = randint(1, 100)
print("'Добро пожаловать в числовую угадайку'")
name = input('Введите Ваше имя: ')


def is_valid(num):
    if not num.isdigit():
        print('Нужно ввести (неотрицательное) ЧИСЛО!')
        return False
    if num.isdigit() and 1 <= int(num) <= 100:
        return num
    if num.isdigit() and int(num) not in range(1, 101):
        print('Число в диапазоне от 1 до 100!')
        return False


while True:
    guess = input(f'Уважаемый(ая) {name}, Введите число от 1 до 100: ')
    if is_valid(str(guess)) is False:
        continue
    elif int(guess) > a:
        print('Слишком МНОГО, попробуйте еще раз!')
    elif int(guess) < a:
        print('Слишком мало, давайте еще разок!')
    elif int(guess) == a:
        print('Вы угадали, поздравляем!')
        break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')