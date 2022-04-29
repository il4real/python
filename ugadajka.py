from random import randint

print("Игра - 'Угадайка число!'")
name = input('Введите Ваше имя: ')
a = randint(1, 100)

while True:
    guess = int(input(f'Уважаемый(ая) {name}, Введите число от 1 до 100: '))
    if guess > a:
        print('Слишком МНОГО, попробуйте еще раз!')
    elif guess < a:
        print('Слишком мало, давайте еще разок!')
    else:
        print('Вы угадали, поздравляем!')
        break