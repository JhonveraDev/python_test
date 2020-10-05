import random

IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


WORDS= [
    'lavadora',
    'gobierno',
    'sofa',
    'diputado',
    'teclado'
]

def random_word():
    indice = random.randint(0, len(WORDS)-1)
    return WORDS[indice]

def display_board(hidden_word,tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('---*---')


def run():
    word=random_word()
    hidden_word=['-'] *len(word) 
    tries=0
 
    
    while True:
        display_board(hidden_word,tries)
        curret_letter = str(input("Escoge una Letra: "))


if __name__ == '__main__':
    
    print("Entrada de juego")
    run()
    