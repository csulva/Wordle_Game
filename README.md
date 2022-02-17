# Wordle_Game

Welcome to my wordle_game!
Challenge yourself and try to guess the correct 5-letter word provided at random each time you play. You will have 6 tries.
If one of the letters in your guess is in the 5-letter word, and in the same position, it will appear in UPPERCASE. That means that letter is correct.
If one of the letters in your guess is in the 5-letter word but in a different position, it will appear in lowercase. That means it will be somewhere else in the answer.

## Play the Game
To test your skills, [play here on Repl.it](https://replit.com/@ChrisSulva/wordlegame#main.py)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install a few required packages:

[Random-Word](https://pypi.org/project/Random-Word/) will help generate a random word for you to guess:

```bash
pip install random-word
```

[PyYAML](https://pypi.org/project/PyYAML/) is also needed for the Random-Word package to work.

```bash
pip install pyyaml
```

## Usage

```python
# Import 5 letter word
from random_word import RandomWords
random_words = RandomWords()
random_word = random_words.get_random_word(hasDictionaryDef="true", minCorpusCount=800, minLength=5, maxLength=5).lower()
```

Example of gameplay:

![Wordle Game in Play](https://media.giphy.com/media/tRc6XpvSdFNnYuYr7T/giphy.gif)


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
