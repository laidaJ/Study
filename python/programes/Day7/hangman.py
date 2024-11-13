import random
from hangman_art import logo, hangman
from hangman_wordlist import word_list

#print logo
print(hangman_art.logo)

lives = 5

chosen_word = random.choice(word_list)
print(f"chosen word is {chosen_word}")

# display the same length of chosen word like ['_', '_', '_']
length_word = len(chosen_word)
display = []
for n in range(length_word):
    display += "_"
print(display)

end_of_game = False

# loop the game if have lives remain and game not end
while not end_of_game: 
    guess = input("Please guess a letter: ").lower()
    if guess in display:
        print(f"You've already guess'd {guess}")
    for position in range(length_word): 
        letter = chosen_word[position]
        if guess == letter:
            display[position] = guess
    if guess not in chosen_word:
        print(f"{guess} is not in the word, now you have {lives} lives remain")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("YOU LOSE!")

    print(display)
    if "_" not in display:
        end_of_game = True
        print("YOU WIN!")
    print(stage[lives])
