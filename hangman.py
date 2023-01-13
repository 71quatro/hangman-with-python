
import random
import os

usedLetters = []
global gameOver
global won

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

# introduction 
def welcome():
    print(" ########################")
    print("#                        #")
    print("#  Welcome to Hang Man!  #")
    print("#                        #")
    print(" ########################")

#hangman drawing
def drawHangman(i):
    for i in range(0 , i):
        print(hangman[i])

#the game
def gameLogic():
    randWord = random.choice(open("words.txt").read().split())
    print("Your word is " + str(len(randWord)) + " letters long. Good Luck!")
    print("You can only guess 1 letter at a time!")
    underscores = []

    for x in range(0, len(randWord)):
        underscores.append("_")
    print("".join(underscores))
    gameOver = False
    currenti = 0
    while(not(gameOver)):
        guess = input("Your guess: ")
        os.system('cls')
        usedLetters.append(guess)

        #compare the guess to the letters in randWord
        for s in range(0,len(randWord)):
            if(guess == randWord[s]):
                underscores[s] = guess

        if(guess not in randWord):
            currenti+=1
        if(currenti > len(hangman)-1):
            won = False
            gameOver = True
            print("You Lost!")
        currentWord = "".join(underscores)
        print(currentWord)

        if (currentWord == randWord):
            gameOver = True
            won = True
            print("You won!")
        drawHangman(currenti)
        print("Used Letters: "+str(usedLetters))

    if(gameOver):
        os.system('cls')
        usedLetters.clear()
        if not won:
            print("You lost! The word was " + randWord + "!\n")
        elif won:
            print("Congratulations! The word was " + randWord + "!\n")
        cont = input("Enter 'y' to play again!: ")
        os.system('cls')
        return cont

def game():
    welcome()
    cont = "y"
    while cont == "y":
        cont = gameLogic()
    print("Thank you for playing!")

def main():
    game()

main()