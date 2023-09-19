import random

words = {
    #'подстаканник': 'подставка под посуду',
    'подушка' : 'то на чём мы спим',
    # 'бутылка':'что-то жидкое внутри',
    # 'сумка':'женщины и мужчины носят это',
    # 'зеркало':'ты можешь себя увидеть',
    # 'компьютер':'то на чём ты можешь работать',
    # 'телефон':'звонки',
    # 'дерево':'зелёное сверху, коричневое снизу',
    # 'лампа':'висит груша, нельзя скушать',
    'ананас':'какой ингредиент содержит своеобразная пицца'
}
lifes = 7
continue_game = 'Y'
words_list = list(words)

print('У вас 7 жизней.')

while continue_game == 'Y' and lifes != 0:
    word = random.choice(words_list)
    words_list.remove(word) #избавились от повторов
    explanation = words[word]
    game_word = '*' * len(word)

    print(explanation)
    print(game_word)

    while game_word.find('*') != -1 and lifes != 0 :
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
                lifes -= 1
                print(f'Введите другую букву. У вас осталось жизней: {lifes}')
            print(game_word)
        else:
            if letter == word:
                game_word = word
                print(word)
                print('Ответ верный!')
            else:
                lifes -= 3
                if lifes < 0:
                    lifes = 0
                print('Ответ неверный!')
                print(f'У вас осталось жизней: {lifes}')

    if words_list != []:
        print('Хотите сыграть ещё? Y/N?')
        continue_game = input() 
    else:
        print('Вы отгадали все слова.')
        continue_game = 'N'
    
print('Игра окончена')


# слова не должны повторяться 

