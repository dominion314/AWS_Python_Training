'''Use deductive logic to figure out a 3 digit number'''

import random

NUM_DIGITS = 3 # Try setting this to 1 or 10
MAX_GUESSES = 10 # Try setting this to 1 or 100

def main():
    print('''
I am thinking of a {}-digit number with no repeared digits.
Try to guess what it is. Here are some clues:

When I say:       That Means:
    Pico          One digit is correct, but in the wrong position.
    Fermi         One digit is correct and in the right position.
    Bagels        No digit is correct.

For example, if the secret number is 248 and your guess was 843, 
the clues would be Germi Pico
'''.format(NUM_DIGITS))

    while True:   #Main game loop
        # This stores the secret number the player needs to guess.
        secretNum = getSecretnum()
        print('I have thought up a number.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until they enter a valid guess
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')
            
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break # break out of the loop if correct
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))
        
        # Ask player if they want to try again
        print('Play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')

def getSecretnum():
    '''Requests a string made up of NUM_DIGITS unqiue random digits and secre'''
    numbers = list('0123456789') # Create a list of digits
    random.shuffle(numbers)# Shuffle them into a random order

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum 

def getClues(guess, secretNum):
    '''Returns atring with the pico, fermi, bagels clues for a guess
    and a secret number pair.'''
    if guess == secretNum:
        return 'You got it!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in correct position.
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # A correct digit is in the wrong postion.
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels' # No digits are in correct position.
    else:
        # Sort the clues into ABC order so their original order
        # doesn't give information away.
        return ' '.join(clues)

# If the program is run (instead of imported), run the game/
if __name__ == '__main__':
    main()

