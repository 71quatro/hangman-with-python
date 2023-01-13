
import random

#global word bank 
wordBank = ["ford", "disneyland", "apple", "red", "america"]
hangman = [  " ___________"
            ,"|     |     |"
            ,"|    ___    |"
            ,"|   |-_-|   |"
            ,"|   \ | /   |"
            ,"|    \|/    |"
            ,"|     |     |"
            ,"|    / \    |"
            ,"|   /   \   |"
            ,"|___________|"
]

emptyHangman = [ " ___________"
                ,"|     |     |"
                ,"|           |"
                ,"|           |"
                ,"|           |"
                ,"|           |"
                ,"|           |"
                ,"|           |"
                ,"|           |"
                ,"|___________|"
]


# introduction 
def welcome():
    print(" ########################")
    print("#                        #")
    print("#  Welcome to Hang Man!  #")
    print("#                        #")
    print(" ########################")
#hangman drawing
def drawFullHangman():
    for h in hangman:
        print(h)

def drawEmptyHangMan():
    for h in emptyHangman:
        print(h)

def gameLogic():
    randWord = wordBank[random.randint(0,len(wordBank) - 1)]
    print("Your word is " + str(len(randWord)) + " letters long. Good Luck!")
    underscores = []
    for x in range(0, len(randWord)):
        underscores.append("_")
    print("".join(underscores))
    guess = input("Your guess: ")
    
#compare the guess to the letters in randWord
    for s in range(0,len(randWord)):
        if(guess == randWord[s]):
            underscores[s] = guess
    print("".join(underscores))

def main():
    welcome()
    gameLogic()

main()