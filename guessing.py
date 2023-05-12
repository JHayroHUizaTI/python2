import random
number = random.randint(1,10)

player_name = input("Hello, what's your name?")
number_of_guesses = 1

print(f"Okay! I am {player_name} guessing a number between 1 and 10")

while number_of_guesses < 5:
    print('*'*10)
    print('ROUND ',number_of_guesses)
    print('*'*10)
    guess = int(input())
    number_of_guesses +=1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print(f"You guessed the number in { number_of_guesses} tries!!!")
else:
    print(f"You did not guess the number, the number was {number}")
