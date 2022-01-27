# Import 5 letter word
from random_word import RandomWords
random_words = RandomWords()
random_word = random_words.get_random_word(hasDictionaryDef="true", minCorpusCount=800, minLength=5, maxLength=5).lower()

# Import time for breaks in the command line
import time

# Ensure the word has only letters
if random_word.isalpha() == False:
    quit()

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

def print_board(board):
    """[Prints the blank board to the console. Will change when it is used
    in the play_game method, so that it replaces the blank spaces with a letter
    if the letter is somewhere in the word/answer.

    Args:
        board (list of lists): A blank board to show which spaces still need to be guessed. (See board above)
    """

    # Length of all rows within the board - 6
    for i in range(len(board)):
        # Length of items in each row - 5 (one for each letter)
        for j in range(len(board[0])):
            print(f"{board[i][j]} | ", end='')
            # Prints new space if row ends
            if j % 4 == 0 and j != 0:
                print('\n')

def play_game(board, word, letters):
    """Plays the wordle game, walking the user through at most 6 guesses to guess the correct word.
    When the word is guessed, all spots will be capitalized and the game will end. If the user does not guess
    the word in 6 tries, the game will end.

    Args:
        board (list of lists): See above, it provides a blank board
        word (string): The random string imported as a 5-letter word
        letters (list): List of strings that shows the letters in the alphabet. If the user has guessed a letter, it will appear in caps.
    """

    print("""Welcome to my wordle_game! To play, try to guess the correct 5-letter word. You will have 6 tries. \n
    If your guess has one of the same letters as the 5-letter word, it will appear in lowercase.\n
    If one of your letters is the same letter in the same spot as the 5-letter word, it will appear in UPPERCASE.\n""")
    time.sleep(1)
    print('Guess the word correctly within 6 attempts and you win! Otherwise try again by clicking "run".')
    row = 0
    attempts = 6
    time.sleep(1)
    # Six tries to win
    while row <= len(board):

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
                # If the letter is correct add it to the puzzle in that place but in uppercase
                if guess[i] == split_word[i]:
                    board[row][i] = guess[i].upper()
                # If the letter is correct in one spot, do not tell the user that letter is still available
                if board[row][i].islower() and num > 1:
                    continue
                # If the letter is correct but in a different spot, add it to the puzzle in that place but lowercase
                elif guess[i] in split_word and guess[i] != split_word[i]:
                    board[row][i] = guess[i].lower()
                else:
                    pass

            # Print the board which will print how you did in that particular row for those guesses
            print_board(board)

            # If all letters in uppercase, you guessed the word correctly
            if all(letter.isupper() for letter in board[row]):
                print(f'You won! The word was "{word}"')
                quit()

            # Print all letters in the alphabet
            print('Guessed letters appear in UPPERCASE: ')
            # If letter has been guessed, make it uppercase
            for letter in guess:
                for l in range(len(letters)):
                    if letter == letters[l]:
                        letters[l] = letter.upper()
            print(letters)

            # After each guess, remove one attempt
            attempts -= 1
            # If attempts run out, user loses and quit the game
            if attempts == 0:
                print(f'Sorry you ran out of attempts.\nThe correct word was "{word}".\nBetter luck next time!')
                quit()
            print(f'You now have {attempts} attempts left...')

            # Move onto the next row in the board
            row += 1

        # Ensures the guess is 5 letters long, otherwise guess again
        else:
            print('Guess must be 5 letters.')
            continue

# Run the game
play_game(board, random_word, letters)