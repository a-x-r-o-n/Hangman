from db import *
def wrongAnswer(numberOfWrongAnswer):
    if numberOfWrongAnswer == 0:
        print("\n\n\t------\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t--------")
    if numberOfWrongAnswer == 1:
        print("\n\n\t------\n\t|    |\n\t|\n\t|\n\t|\n\t|\n\t|\n\t--------")
    elif numberOfWrongAnswer == 2:
        print("\n\n\t------\n\t|    |\n\t|    O\n\t|\n\t|\n\t|\n\t|\n\t--------")
    elif numberOfWrongAnswer == 3:
        print("\n\n\t------\n\t|    |\n\t|    O\n\t|    |\n\t|\n\t|\n\t|\n\t--------")
    elif numberOfWrongAnswer == 4:
        print("\n\n\t------\n\t|    |\n\t|    O\n\t|   /|\n\t|\n\t|\n\t|\n\t--------")
    elif numberOfWrongAnswer == 5:
        print("\n\n\t------\n\t|    |\n\t|    O\n\t|   /|\\\n\t|\n\t|\n\t|\n\t--------")
    elif numberOfWrongAnswer == 6:
        print("\n\n\t------\n\t|    |\n\t|    O\n\t|   /|\\\n\t|   /\n\t|\n\t|\n\t--------")
    elif numberOfWrongAnswer == 7:
        print("\n\n\t------\n\t|    |\n\t|    O\n\t|   /|\\\n\t|   / \\\n\t|\n\t|\n\t--------")
    elif numberOfWrongAnswer == 8:
        print("\n\n     _______\n    |       |\n    |       \n    |       \n    |      \n    |      \\O/\n    |       |\n    |      / \\\n    |\n\nCongratulations! 🎉\nYou've Won!")
def displayQuestionDash(spots,alphabetPresent):
    for i in spots:
        if i in alphabetPresent:
            print(i,end=' ')
        elif i != " ":
            print("-",end=' ')
        elif i == " ":
            print("\t",end=' ')