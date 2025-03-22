# -*- coding: utf-8 -*-
"""
Chris Tison
CIS256 Spring 2025
EX 4
Test of Word Guessing Game

Wasnt quite sure about testing when using user inputs, so it is really just testing the logic
of the code from my guessing game.
"""

import pytest
import random
from guess_the_word import word_list

def test_word_selection():
    """This function randomly chooses a word form the word list imported
    from my game, then checks if it is in the list."""
    
    selected_word = random.choice(word_list)
    assert selected_word in word_list


def test_correct_guess_processing():
    """This sets the word to dishwasher...and tests a couple of correct guesses
    as well as checking that list of guessed letters is updated,
    as well as checking number of attempts is still correct."""
    # Simulate the hangman game
    word = 'dishwasher'  # Example word
    guessed_word = ['_'] * len(word)
    attempts = 6 # Initialize number of guesses
    guessed_letters = [] # Initialize the guessed letters list.

    # Simulate correct guesses and also 1 incorrect guess
    for guess in ['a','e','y']:
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
       
        else:
            attempts -= 1
        guessed_letters.append(guess)

    # Check if the guessed word is updated correctly
    assert guessed_word == ['_', '_', '_', '_', '_', 'a', '_', '_','e', '_']
    assert guessed_letters == ['a','e','y'] # Check guesses are appended
    assert attempts == 5  # 1 incorrect guess drops count from 6 to 5


if __name__ == '__main__':
    pytest.main()
