# Hangman Game
# Python Language: Object Oriented Programming - OOP
# By sabrinaamorimdecastro

# Import package for random selection of the word in date.txt
import random

# Board with the 6 possible positions
board = ['''

--------*- Hangman -*--------

    +---+
    |   |
    |
    |
    |
    |
=========''', '''

    +---+
    |   |
    |   O
    |
    |
    |
=========''', '''

    +---+
    |   |
    |   O
    |   |
    |
    |
=========''', '''

    +---+
    |   |
    |   O
    |  /|
    |
    |
=========''', '''

    +---+
    |   |
    |   O
    |  /|\ 
    |
    |
=========''', '''

    +---+
    |   |
    |   O
    |  /|\ 
    |  /
    |
=========''', '''

    +---+
    |   |
    |   O
    |  /|\ 
    |  / \ 
    |
=========''']


# Class
class Hangman:

    # Method Constructor
    def __init__(self, word):
        self.word = word
        self.missed_letters = []
        self.guessed_letters = []

    # Method for try a letter
    def guess(self, letter):
        if letter in self.word and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
        elif letter not in self.word and letter not in self.missed_letters:
            self.missed_letters.append(letter)
        else:
            return False
        return True
        
    # Method for verify if lost the game
    def hangman_over(self):
        return self.hangman_won() or (len(self.missed_letters) == 6)

    # Method for verify if won the game
    def hangman_won(self):
        if '_' not in self.hide_word():
            return True
        return False

    # Method for hide the letters
    def hide_word(self):
        rtn = ''
        for letter in self.word:
            if letter not in self.guessed_letters:
                rtn += '_'
            else:
                rtn += letter
        return rtn

    # Method for chech the game status and print the board on screen
    def print_game_status(self):
        print(board[len(self.missed_letters)])
        print('\nPalavra: ' + self.hide_word())
        print('\nLetras erradas: ',)

        for letter in self.missed_letters:
            print (letter,)
        print()
        print('Letras corretas',)

        for letter in self.guessed_letters:
            print(letter,)
        print ()

# Function for read the word randomly on the file
def rand_word():
    with open("date.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()

# Function Main - Program Execution
def main():

    # Object
    game = Hangman(rand_word())

    # While the game is not over, Print status, request a letter and read character
    while not game.hangman_over():
        game.print_game_status()
        user_input = input('\nDigite uma letra: ')
        game.guess(user_input)

    # Verify the game status
    game.print_game_status()

    # According with the status, print a message on screen for the player
    if game.hangman_won():
        print('\nParabéns! Você vencer!')
    else:
        print('\nFim de joog! Você perdeu.')
        print('\nA palavra era ' + game.word)

# Execute the program
if __name__ == "__main__":
    main()
