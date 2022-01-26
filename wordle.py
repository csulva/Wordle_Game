# Import 5 letter word and split
from random_word import RandomWords

random_words = RandomWords()

random_word = random_words.get_random_word(hasDictionaryDef="true", minLength=5, maxLength=5)

# Print list of letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Create check word function
# If letter is correct place, uppercase, if wrong place, lowercase
# If not correct, _
# If word complete, congrats and quit


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

# print_board(board)

def play_game(board, word, letters):
    x = 0
    attempts = 6
    while x <= len(board):
        guess = input('Guess a 5-letter word: ').lower()
        if len(guess) == 5 and guess.isalpha:
            guess = [letter for letter in guess]
            split_word = [letter for letter in word]
            for i in range(len(guess)):
                num = split_word.count(guess[i])
                if guess[i] == split_word[i]:
                    board[x][i] = guess[i].upper()
                if board[x][i].isupper() and num == 1:
                    continue
                elif guess[i] in split_word and guess[i] != split_word[i]:
                    board[x][i] = guess[i].lower()
                else:
                    pass
            print_board(board)
            if all(letter.isupper() for letter in board[x]):
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
            x += 1
        else:
            print('Guess must be 5 letters.')
            continue

play_game(board, random_word, letters)