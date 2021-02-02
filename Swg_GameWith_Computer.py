import random


def game(a, b):
    if (a == 's' and b == 'w') or (a == 'w' and b == 'g') or (a == 'g' and b == 's'):
        return 'c'
    if (a == 'w' and b == 's') or (a == 'g' and b == 'w') or (a == 's' and b == 'g'):
        return 'u'
    elif a == b:
        return 0


def swg():
    choices = range(10)
    resultDic = []
    gameChoice = {
        's': 'Snake',
        'w': 'Water',
        'g': 'Gun'
    }
    computerScore = 0
    userScore = 0
    for x in choices:
        computerChoice = random.choice(("s", "w", "g"))
        wFlag = False
        while not wFlag:
            userChoice = input("Select S for snake,W for water and G for gun: ").lower()
            if userChoice == "s" or userChoice == "w" or userChoice == 'g':
                wFlag = True
                result = game(computerChoice, userChoice)
                if result == 'u':
                    userScore += 1
                    resultDic.append(
                        {'Computer Choice': gameChoice[computerChoice], 'User Choice': gameChoice[userChoice],
                         'Result': 'You Won'})

                    for i in resultDic:
                        print(i)

                elif result == 'c':
                    computerScore += 1
                    resultDic.append(
                        {'Computer Choice': gameChoice[computerChoice], 'User Choice': gameChoice[userChoice],
                         'Result': 'Computer Won'})
                else:
                    resultDic.append(
                        {'Computer Choice': gameChoice[computerChoice], 'User Choice': gameChoice[userChoice],
                         'Result': 'It Tie'})

                    for i in resultDic:
                        print(i)

        if x == choices[-1]:
            print("Game Over")

    if computerScore > userScore:
        print("You Lose game, Final Score is Computer: {s1}, Your: {s2}".format(s1=computerScore, s2=userScore))
    elif userScore > computerScore:
        print("You Won game, Final Score is Computer: {s1}, Your: {s2}".format(s1=computerScore, s2=userScore))
    elif userScore == computerScore:
        print("It Tie, Final Score is Computer: {s1}, Your: {s2}".format(s1=computerScore, s2=userScore))


swg()
