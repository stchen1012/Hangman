#create hangman game

import random
import re

word_list = ["dictionary", 'cat', "emotion", "tempting", "intrigue", "happiness", "rant", "interest"]
random.shuffle(word_list)

random_word = random.choice(word_list)
#print(random_word)

guesses = []
player_word_guess = []
hangman_body = ["rope", "head", "body", "right arm", "left arm", "right leg", "left leg"]

for letter in range(len(random_word)):
    player_word_guess.append("___")

game_over = False
counter = 0
counter2 = 1

while game_over != True:
    player_guess = input("Guess a letter: ")
    if not re.match("[a-z]", player_guess):
        print("Please only enter letters. Try again.")
    elif player_guess in guesses:
        print("You've already guess this")
    else:
        for position in range(len(random_word)):
            if player_guess == random_word[position]:
                player_word_guess[position] = player_guess
        # added in code to track hangman graphic in word form
        if player_guess not in random_word:
            print(hangman_body[:counter2])
            counter2 += 1

        print(player_word_guess)
        list_checker = ''.join(player_word_guess)
        #print(list_checker)

        if list_checker == random_word:
            print("You win!")
            game_over = True

        guesses.append(player_guess)
        counter += 1
        print("\n")
        print("Previous guesses:" + str(guesses))
        print("This is how many times you have guessed: " + str(counter))
        print("\n")
