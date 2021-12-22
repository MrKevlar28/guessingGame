Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import random
print("Number Guessing Game")
Number Guessing Game
number = random.randint(1,9)
chances = 0
print("Guess a number (between 1 and 9):")
Guess a number (between 1 and 9):
while chances < 5:
    guess = int(input("Enter your guess : "))
    if guess == number:
        print("Congratulations you won!!")
        break
    elif guess < number:
        print("Your guess was too low: Try guessing a number higher than", guess)
    else:
        print("Your guess was too high: Try guessing a number lower than", guess)
    chances += 1
    if not chances < 5:
        print("You lose!! The number is", number)

        
Enter your guess : 9
Your guess was too high: Try guessing a number lower than 9
Enter your guess : 5
Your guess was too low: Try guessing a number higher than 5
Enter your guess : 7
Your guess was too high: Try guessing a number lower than 7
Enter your guess : 6
Congratulations you won!!
