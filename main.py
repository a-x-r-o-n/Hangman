from db import *
from module import *
import random
mv = random.choice(movies).lower()
stringToList = []
attempt = []
guess = []
for j in mv:
    if j not in stringToList and j != " ":
        stringToList.append(j)
count = 0
while count<=6:
    print("\n\nMovie Hint:-\t",end='')
    displayQuestionDash(mv,guess)
    print("\n\n")

    g = input("\n\nEnter Character: ")
    if g in attempt:
        print(f"\n\nLetter {g} is already entered try a different one") 
    elif g in stringToList:
        print(f"\n\nYour Guess was Correct!!\n\'{g}\' is there in the movie name")
        guess.append(g)
    elif g not in stringToList:
        count += 1
        print(f"\n\nAlphabet \'{g}\' was not there in the movie name")
        print("\n\n")
    if len(stringToList) == len(guess):
        wrongAnswer(8)
        print(f"\n\nYou Guessed all Characters the thing is \"{mv}\"")
        break
    attempt.append(g)
    wrongAnswer(count)
    print(f"\n\nNumber of Wrong Answers: {count}")
    print(f"Correct Alphabets guessed: {guess}")