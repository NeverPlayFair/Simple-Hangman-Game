import random

#Author NeverPlayFair

def hangman():
    words = random.choice(["jazz","buzz","quiz","beautiful","recommend","puff","fox","grey","friend","word"])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    rounds = 10
    guessmade = ''


    while len(words) > 0:
        main = ""
        missed = 0

        for letter in words:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == words:
            print(main)
            print("You win!", "congratulations", nickname)
            break
        print("Guess the word:", main)
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()
        if guess not in words:
            rounds = rounds - 1
        if rounds == 9:
            print("9 turn left")
            print("   ---------   ")
        if rounds == 8:
            print("8 turns left")
            print("   ---------   ")
            print("       0       ")
        if rounds == 7:
            print("7 turns left")
            print("   ---------   ")
            print("       0       ")
            print("       |       ")
        if rounds == 6:
            print("6 turns left")
            print("   ---------   ")
            print("       0       ")
            print("       |       ")
            print("      /        ")
        if rounds == 5:
            print("5 turns left")
            print("   ---------   ")
            print("       0       ")
            print("       |       ")
            print("      / \      ")
        if rounds == 4:
            print("4 turns left")
            print("   ---------   ")
            print("     \ 0       ")
            print("       |       ")
            print("      / \      ")
        if rounds == 3:
            print("3 turns left")
            print("   ---------   ")
            print("     \ 0 /     ")
            print("       |       ")
            print("      / \      ")
        if rounds == 2:
            print("2 turns left")
            print("   ---------   ")
            print("     \ 0 /|    ")
            print("       |       ")
            print("      / \      ")
        if rounds == 1:
            print("1 turns left")
            print("Last chance!")
            print("   ---------   ")
            print("     \ 0_|/    ")
            print("       |       ")
            print("      / \      ")
        if rounds == 0:
            print("You lose!")
            print("Just look the man is already dead!")
            print("   ---------   ")
            print("       0_|     ")
            print("      /|       ")
            print("      / \      ")





nickname = input("Enter your nickname here :)! ")
print("Welcome there", nickname)
print("--------------------")
print("Guess the word in less than 10 attempts. Enjoy and try good luck!")
hangman()
print()
