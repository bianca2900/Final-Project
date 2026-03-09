import random

if __name__ == '__main__':
    questionnaire = {
        'Which of the following decribes \'a pasta with few ingredients?\'': ['putanesca', 'spaghetti', 'rigatoni', 'lasagna'],
        'Which of the following pastas contains cheese, bacon, and an egg?': ['carbonara', 'gnocci', 'ziti', 'ragu'],
        'What is the capital of Italy?': ['Rome', 'Venice', 'Florence', 'Milan']
        ''
    }

    random_pair = random.choice(list(questionnaire.items()))
    question, answers = random_pair 

    print(question)

    # TODO randomize order of list ...
    i = 1
    for answer in answers:
        print(str(i) + ') ' + answer)
        i += 1

    response = input('')

    if response == answers[0]:
        print('correct!')
    else:
        print('incorrect!')

