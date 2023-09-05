import random

words = {
    'подстаканник': 'подставка под посуду',
    'подушка' : 'то на чём мы спим',
    'бутылка':'что-то жидкое внутри',
    'сумка':'женщины и мужчины носят это',
    'зеркало':'ты можешь себя увидеть'
}

words_list = list(words)

word = random.choice(words_list)
explanation = words[word]
game_word = '*' * len(word)

print(explanation)
print(game_word)

while game_word.find('*') != -1:
    print('ВВедите букву')
    letter =  input()
    if word.find(letter) != -1:
        game_word = list(game_word)
        for i in range(0, len(word)):
            if word[i] == letter:
                game_word[i] = letter
        game_word = ''.join(game_word)
    print(game_word)

# game_word = list(game_word)
# game_word[0] = 'k'
# game_word = ''.join(game_word)
# print(game_word)