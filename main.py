import os
import hangman_art
import data_base
print(hangman_art.logo)
# Generate random word
import random
pc_guess = random.choice(data_base.word_list)
# print(pc_guess)
# for qty use to len(pc_guess)
length = len(pc_guess)
lives = 6
blanks_avilable = True
# -----below code only works once but we need it unless all dash fillip  for this using while
blanks = []
# using loop to perform iteration replace letter with blanks
for x in range(length):
    # using +=assigned operator
    blanks += "_"

print(blanks)
while blanks_avilable:

    # 3-Ask the user to guess a letter-severally
    user_guess = input("Entered the user Guess letter one by one:  ")
    os.system('cls')
    #user guess already exist in blanks "_"
    if user_guess in blanks:
        print(F"this letter {user_guess} is already guessed it")
    #"_"Dash position
    for position in range(length):
        letter = pc_guess[position]
        # print(letter)
        # apply if letter matched with user_guess
        if letter == user_guess:
            # if matched take position with blanks-mean indexing[]
            blanks[position] = letter
    print(blanks)
    if user_guess in pc_guess:
        print(hangman_art.stages[lives])
    else:
        lives = lives -1
        print(hangman_art.stages[lives])
        print(F"you guess letter {user_guess} not in word")
        if (lives==0):
            print("You Lose! GAME OVER")
            blanks_avilable = False
    # -----while loop to infite unless dont give stop/break  here provide while loop false to stop it.
    # this is membership operatore use to find "_" in blanks
    if "_" not in blanks:
        print("You WON")
        blanks_avilable = False
        print("Do you want to continue again?")


print(hangman_art.logo)