# Import 5 letter word
from random_word import RandomWords
random_words = RandomWords()
random_word = random_words.get_random_word(hasDictionaryDef="true", minLength=5, maxLength=5)

# Import time module
import time

# List of letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

board = [
    ['_','_','_','_','_',],
    ['_','_','_','_','_',],
    ['_','_','_','_','_',],
    ['_','_','_','_','_',],
    ['_','_','_','_','_',],
    ['_','_','_','_','_',],
]

# Print board
def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(f"{board[i][j]} | ", end='')
            if j % 4 == 0 and j != 0:
                print('\n')

# Create check word function
# If letter is correct place, uppercase, if wrong place, lowercase
# If not correct, _
# If word complete, congrats and quit
def play_game(board, word, letters):
    print('Welcome to my wordle_game! To play, try to guess the correct 5-letter word. You will have 6 tries.\
    If your guess has one of the same letters as the 5-letter word, it will appear in lowercase.\
    If one of your letters is the same letter in the same spot as the 5-letter word, it will appear in UPPERCASE.')
    row = 0
    attempts = 6
    # Six tries to win
    while row <= len(board):
        time.sleep(1)

        # Guess the word via the console... must be five letters
        guess = input('Guess a 5-letter word: ').lower()
        if len(guess) == 5 and guess.isalpha:
            # Split the guessed word into individual characters
            guess = [letter for letter in guess]
            # Split the answer into individual characters
            split_word = [letter for letter in word]

            # Iterate through the letters of the guess
            for i in range(len(guess)):
                # Check how many of each letter
                num = split_word.count(guess[i])
                # If the letter is correct add it to the puzzle in that place
                if guess[i] == split_word[i]:
                    board[row][i] = guess[i].upper()
                if board[row][i].isupper() and num == 1:
                    continue
                elif guess[i] in split_word and guess[i] != split_word[i]:
                    board[row][i] = guess[i].lower()
                else:
                    pass
            print_board(board)
            if all(letter.isupper() for letter in board[row]):
                print(f'You won! The word was "{word}"')
                quit()
            print('Unguessed letters appear in lowercase: ')
            for letter in guess:
                for l in range(len(letters)):
                    if letter == letters[l]:
                        letters[l] = letter.upper()
            print(letters)
            attempts -= 1
            if attempts == 0:
                print(f'Sorry you ran out of attempts.\nThe correct word was "{word}".\nBetter luck next time!')
                quit()
            print(f'You now have {attempts} attempts left...')
            row += 1
        else:
            print('Guess must be 5 letters.')
            continue

play_game(board, random_word, letters)