import random

word_list = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа',
             'слово', 'место', 'лицо', 'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай',
             'голова', 'ребенок', 'сила', 'конец', 'вид', 'система', 'часть', 'город', 'отношение', 'женщина',
             'деньги', 'земля', 'машина', 'вода', 'отец', 'проблема', 'час', 'право', 'нога', 'решение', 'дверь',
             'образ', 'история', 'власть', 'закон', 'война', 'бог', 'голос', 'тысяча', 'книга', 'возможность',
             'результат', 'ночь', 'стол', 'имя', 'область', 'статья', 'число', 'компания', 'народ', 'жена',
             'группа', 'развитие', 'процесс', 'суд', 'условие', 'средство', 'начало', 'свет', 'пора', 'путь', 'душа']


def get_word():
    return random.choice(word_list).upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def print_word(word_, list_):
    for c in word_:
        if c in list_:
            print(c, end=' ')
        else:
            print('_', end=' ')
    print()


def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    print("Let's play GUESS THE WORD")
    print('Below you can see, how many letters in this word')
    print(word_completion)

    while tries != -1:
        print('Tries left: ' + str(tries))
        if tries == 0:
            print('You lost, word was - ' + word)
            print(display_hangman(tries))
            prodolzhenie = input('Do you wanna play again? If yes, enter "y", or press ENTER to leave')
            if prodolzhenie == 'y':
                play(get_word())
            else:
                print('Bye-bye')
                break

        print(display_hangman(tries))
        let_word = input('Enter word or letter in russian: ').upper()

        if not let_word.isalpha():
            print('Entered symbol(s) are not letters, try again!')
            continue

        if len(let_word) == 1:
            if let_word not in guessed_letters:
                if let_word in word:
                    guessed_letters.append(let_word)
                    for c in word:
                        if c not in guessed_letters:
                            print('Guessed letter!')
                            print_word(word, guessed_letters)
                            guessed = False
                            break
                        guessed = True
                    if guessed:
                        print_word(word, guessed_letters)
                        print('Congrats, you guessed the word!')
                        prodolzhenie = input('Do you wanna play again? If yes, enter "y", or press ENTER to leave')
                        if prodolzhenie == 'y':
                            play(get_word())
                        else:
                            print('Bye-bye')
                            break
                tries -= 1
            else:
                print('This letter already exit, enter another one.')
                continue

        if len(let_word) > 1:
            if let_word not in guessed_words:
                guessed_words.append(let_word)
                if let_word == word:
                    print('Поздравляем, вы угадали слово! Вы победили!')
                    prodolzhenie = input('Do you wanna play again? If yes, enter "y", or press ENTER to leave')
                    if prodolzhenie == 'y':
                        play(get_word())
                    else:
                        print('Bye-bye')
                        break
                if let_word != word:
                    print('Try again. This time you was wrong!')
                    tries -= 1
            else:
                print('Already mentioned, enter another word, please.')
                continue


print(play(get_word()))
