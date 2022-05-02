from random import randint

a = randint(1, 100)
print("'Добро пожаловать в числовую угадайку'")
name = input('Введите Ваше имя: ')


def is_valid(num):
    if int(num) in range(1, 101):
        return int(num)
    else:
        return False


while True:
    guess = int(input(f'Уважаемый(ая) {name}, Введите число от 1 до 100: '))
    if is_valid(guess) is False:
        print('not in range, once more')
        continue
    if guess > a:
        print('Слишком МНОГО, попробуйте еще раз!')
    elif guess < a:
        print('Слишком мало, давайте еще разок!')
    else:
        print('Вы угадали, поздравляем!')
        break
