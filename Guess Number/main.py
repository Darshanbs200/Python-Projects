import random

def guess(a):
    random_number = random.randint(1,a)
    guess = 0
    while guess != random_number:
        guess= int(input(f"Guess the number in between 1 and {a} :"))
        if guess < random_number:
            print('Sorry,guess again.Too low')
        elif guess > random_number:
            print('Sorry,guess again.Too high')
    print(f'yay,Congrats.You have  guessed correct number {random_number}')

guess(10)