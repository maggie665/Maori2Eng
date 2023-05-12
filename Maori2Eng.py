import random

Maori = ['tahi', 'rua', 'toru', 'wha', 'rima', 'ono', 'whitu', 'waru', 'iwa', 'tekau', 'kia ora', 'haere ra',
         'morena', 'ka kite ano', 'haere mai', 'ka pai', 'kei te pai', 'kino', 'whanau', 'iwi', 'tai', 'hui',
         'karakia', 'waiata', 'pakipaki', 'kai', 'katao', 'waka', 'marae', 'ma', 'pango', 'whero', 'paraone',
         'karaka', 'kowhai', 'kakariki', 'kahurangi', 'poroporo', 'rahina', 'ratu', 'raapa', 'rapare', 'ramere',
         'rahoroi', 'ratapu', 'aotearoa', 'motu', 'hotaka', 'wahine', 'tane']
EnglishTranslation = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'hello',
                      'good bye', 'good morning', 'see you later', 'welcome', 'good', ' well done', 'bad', 'family',
                      'tribe', 'friend', 'meeting', 'prayer', 'song', 'clap', 'food', 'water', 'canoe', 'meeting house',
                      'white', 'black', 'red', 'brown', 'orange', 'yellow', 'green', 'blue', 'purple', 'monday',
                      'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'zealand', 'island',
                      'program', 'woman', 'man']

# len_Maori = len(Maori)
# len_EnglishTranslation = len(EnglishTranslation)
random_question = random.sample(list(range(50)), 10)
print(1, random_question)
# print(len(random_question))
i = 0
score = 0
print('Welcome to Maori Translation Game System!\n'
      'Which model do you want to chose?\n'
      '1.Multiple Choice\n'
      '2.Type Answers\n')
a = int(input('Please type 1 or 2 , make your choice.'))
print('*****************************************\n'
      '*****************************************\n')
if a == 1:
    while i <= len(random_question):
        # new_Maori list for options
        # print(2, random_question[i])
        new_Maori = Maori[:]
        del new_Maori[random_question[i]]
        # print(3, Maori)
        random_options = random.sample(list(range(49)), 3)
        # l is for answer list
        l = [random_question[i]]
        # print(4, l)
        new_random_options = l + random_options
        # print(5, new_random_options)
        shuffle_new_radom_options = new_random_options[:]
        random.shuffle(shuffle_new_radom_options)
        # print(6, shuffle_new_radom_options)
        print(
            f'Q{i + 1}. Please choose the correct translation for "{Maori[random_question[i]]}" from the four options.')
        for n in shuffle_new_radom_options:
            print(shuffle_new_radom_options.index(n) + 1, '.', EnglishTranslation[n])
        q1 = int(input('Your choice is ', ))
        # print(q1)
        # print(EnglishTranslation[i])
        if shuffle_new_radom_options[q1 - 1] == new_random_options[0]:
            print(new_random_options[0])
            print(random_question[i])
            print('"Correct!Good!"')
            score += 1
            print('Your score is ，', score)
        else:
            print("Incorrect! The correct answer is'", EnglishTranslation[random_question[i]], " '\n"
                                                                                               "Your score is", score)
        print('*****************************************\n'
              '*****************************************\n')
        i += 1
else:
    s = 0
    while s <= len(random_question):
        # print(s)
        # print(random_question[s])
        q1 = input(f'{s+1}. Please translate "{Maori[random_question[s]]}" into English: ').lower()
        if q1 == EnglishTranslation[random_question[s]]:
            # print(random_question[s])
            print('"Correct!Good!"')
            score += 1
            print('Your score is ', score)
        else:
            print("Incorrect! The correct answer is'", EnglishTranslation[random_question[s]], " '\n"
                                                                                               "Your score is", score)
            print('*****************************************\n'
                  '*****************************************\n')
        s += 1

print(f'Good Job！Your final score is {score}')

