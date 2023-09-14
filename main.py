import random

words = {
    'подстаканник': 'подставка под посуду',
    'подушка' : 'то на чём мы спим',
    'бутылка':'что-то жидкое внутри',
    'сумка':'женщины и мужчины носят это',
    'зеркало':'ты можешь себя увидеть',
    'компьютер':'то на чём ты можешь работать',
    'телефон':'звонки',
    'дерево':'зелёное сверху, коричневое снизу',
    'лампа':'висит груша, нельзя скушать',
    'ананас':'какой ингредиент содержит своеобразная пицца'
}
continue_game = 'Y'
words_list = list(words)

while continue_game == 'Y':
    word = random.choice(words_list)
    explanation = words[word]
    game_word = '*' * len(word)

    print(explanation)
    print(game_word)

    while game_word.find('*') != -1:
        print('Введите букву или слово')
        letter =  input()
        if len(letter) == 1:
            if word.find(letter) != -1:
                game_word = list(game_word)
                for i in range(0, len(word)):
                    if word[i] == letter:
                        game_word[i] = letter
                game_word = ''.join(game_word)
            else:
                print('Введите другую букву')
            print(game_word)
        else:
            if letter == word:
                game_word = word
                print(word)
                print('Ответ верный!')
            else:
                print('Ответ неверный!')

    print('Хотите сыграть ещё? Y/N?')
    continue_game = input() 
    
print('Игра окнчена')


# слова не должны повторяться 

