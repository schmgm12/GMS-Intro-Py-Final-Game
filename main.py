## How many multiplication problems can you solve in 1 minute??
from random import randint
import time
import pandas as pd

def game_choice():
    print('Which game do you want to play?:')
    print('A: Multiplication Challenge')
    print('B: Addition Challenge')
    game = input().lower()

    while game not in ('a', 'b'):
        print('Please enter a valid choice: A or B')
        game = input().lower()
    return game

def get_high_score(game):

    if game == 'a':
        data = pd.read_csv('multiplication_scores.csv', sep=",", header = 0)
        name = data.ix[0, 'Name']
        score = data.ix[0, 'Score']
        message = 'The Multiplication Game high score is held by {} who solved {} problems'.format(name, score)
        return message, score
    else:
        data = pd.read_csv('addition_scores.csv', sep=",", header = 0)
        name = data.ix[0, 'Name']
        score = data.ix[0, 'Score']
        message = 'The Addition Game high score is held by {} who solved {} problems'.format(name, score)
        return message, score

def update_high_score(game, new_name, correct):

    if game == 'a':
        data = pd.read_csv('multiplication_scores.csv', sep=",", header = 0)
        data.ix[0, 'Name'] = new_name
        data.ix[0, 'Score'] = correct
        data.to_csv('multiplication_scores.csv', index = False)
        message = 'Congratulations, {}, you now hold the Multiplication game high score!'.format(new_name)
        print(message)
    else:
        data = pd.read_csv('addition_scores.csv', sep=",", header = 0)
        data.ix[0, 'Name'] = new_name
        data.ix[1, 'Score'] = correct
        data.to_csv('addition_scores.csv', index = False)
        message = 'Congratulations, {}, you now hold the Addition game high score!'.format(new_name)
        print(message)


def multiplication_game():
## generates two random numbers and ask for their product
    x = randint(0, 11)
    y = randint(0, 11)

    answer = int(input('What is {} * {}?\n'.format(x, y)))
    if answer == x * y:
        print('Correct!')
        return 1
    else:
        print('Incorrect')
        return 0

def addition_game():
## generates two random numbers and ask for their sum
    x = randint(0, 100)
    y = randint(0, 100)

    answer = int(input('What is {} + {}?\n'.format(x, y)))
    if answer == x + y:
        print('Correct!')
        return 1
    else:
        print('Incorrect')
        return 0

def main():

    print('Welcome!')
    print('How many problems can you solve in 1 minute?\n')
    game = game_choice()
    message, high_score = get_high_score(game)
    print(message)
    correct = 0

    end_time = time.time() + 60
    while True:
        if time.time() > end_time:
            print('Time is up!')
            print('You answered {} problems correctly.'.format(correct))

            if correct > high_score:
                print('Congratulations, you beat the high score!')
                new_name = input('What is your name?  ')
                update_high_score(game, new_name, correct)
            else:
                response = input('You got {} correct ... that\'s not enough to beat the high score... want to play again? y or n?'.format(correct))
                if response in ('y', 'Y', 'YES', 'yes', 'Yes'):
                    main()
            break
        elif game == 'a':
            correct = correct + multiplication_game()
        elif game == 'b':
            correct = correct + addition_game()

if __name__ == '__main__':
    main()
