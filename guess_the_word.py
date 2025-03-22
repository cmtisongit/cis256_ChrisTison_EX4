# -*- coding: utf-8 -*-
"""
Chris Tison
CIS256 Spring 2025
EX 4
Word Guessing Game
"""

import random

# List of predefined words
word_list = ['dishwasher', 'stove', 'pantry', 'closet', 'attic', 'carpet', 'toilet', 'microwave']

# Function i called hangman because it reminded me the word guessing game.
def hangman():
    # Select a random word from the list, and find the length of the word for use later.
    word = random.choice(word_list)
    word_length = len(word)
    
    # Create a string of underscores the same length of the word to be guessed
    # This is to show the player how many letters there are and serve as placeholders
    guessed_word = ['_'] * word_length
    
    # Number of incorrect guesses allowed
    attempts = 6
    
    # List to track letters already guessed 
    guessed_letters = []  
    
    # Print statments to set up and explain game to player
    print("Welcome to GUESS THE WORD!!!")
    print("These words are things you can find in a house.")
    print(f"Guess the word: {' '.join(guessed_word)}")
    print(f"You have {attempts} attempts remaining.")
    
    # While loop that executes the game as long as there are guesses remaining.
    while attempts > 0:
        # Get the user input for letter... convert to lower case since all words are lower in list
        guess = input("Guess a letter: ").lower() 
        
        # Data validation to make sure only one char is entered and that is not a number.
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        
        # This checks to make sure player has not guessed that letter more than once.
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue
        
        # If it is a newley guessed letter it will add that to the list.
        guessed_letters.append(guess)
        
        # Check if the guessed letter is in the word.
        if guess in word:
            print(f"CORRECT!!! {guess} is in the word.\n")
            
            # When correct guess... update the underscore at the location with the
            # letter that was correctly guessed.
            for i in range(word_length):
                if word[i] == guess:
                    guessed_word[i] = guess
        
        #  Inform player of wrong guess and count down the attempts
        else:
            attempts -= 1
            print(f"WRONG! {guess} is not in the word. You have {attempts} attempts remaining.\n")
        
        # Show the current guessed word
        print(f"Current word: {' '.join(guessed_word)}")
        
        # Check if the word is fully guessed
        if '_' not in guessed_word:
            print(f"Congratulations! You've guessed the word: {''.join(guessed_word)}")
            break
    
    if attempts == 0:
        print(f"Game Over! The word was: {word}")

# Added so it wont run when called by the test program.
if __name__ == '__main__':
    hangman()
