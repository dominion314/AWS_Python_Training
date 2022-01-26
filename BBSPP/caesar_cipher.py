'''
Caesar Cipher is a shift cipher that uses addition and subtraction
to encrypt and decrypt letters.
'''

try:
    import pyperclip # Copies text to clipboard
except:
    pass # If pyperclip is not installed, do nothing.

# Every possible symbol that can be encrypted/decrypted
#(!) You can add numbers and punctuation marks to encrypt those symbols

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'

print('Caesar Cipher')
print('The Caesar Cipher encrypts letters by shfiting them over by a')
print('key number. For example, a key of 2 means the letter A is')
print('encrypted to C, the letter B encrypted to D, and so on.')
print()

# Let the user enter if they are encrypting or decrypting
while True: # Keep asking until the user enters e or d
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    respone = input('> ').lower()
    if respone.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter e or d')

# Let the user enter the key to use
while True: # Keep asking until the user enters a valid key
    maxKey = len(SYMBOLS) - 1
    print('Please enter the key (0 to {}) to use.'.format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue
    
    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

# Let the user enter the message to encrypt/decrypt
print('Enter the message to {}.'.format(mode))
message = input('> ')

# Caesar ciper only works on upper case letters
message = message.upper()

# Stores the encrypted/decrypted form of the message
translated = ''

# Encrypt/decrypt each symbol in the message
for symbol in message:
    if symbol in SYMBOLS:
        # Get the encrypted or decrypted number for this symbol
        num = SYMBOLS.find(symbol) # Get the number of the symbol
        if mode == 'encrypt':
            num = num + key 
        elif mode == 'decrypt':
            num = num - key

        # Handle the wrap-around if the num is larger than the length
        # of SYMBOLS or less than 0
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        # Add encrypted/decrypted numbers symbol to translated
        translated =  translated + SYMBOLS[num]
    else:
        # Just add the symbol without encrypting/decrypting
        translated = translated + symbol

# Display the encrypted/decrypted string to the screen
print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard.'.format(mode))
except:
    pass # Do nothing if pyperclip not installed

'''
Coding Challenges:

What happens if you change SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' on line 16 to SYMBOLS = 'ABC'?
What happens when you encrypt a message with key 0?
What error message do you get if you delete or comment out translated = '' on line 56?
What error message do you get if you delete or comment out key = int(response) on line 45?
What happens if you change translated = translated + SYMBOLS[num] on line 76 to translated = translated + symbol?
'''
