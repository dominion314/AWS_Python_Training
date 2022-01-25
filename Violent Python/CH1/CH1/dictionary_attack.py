'''
Dictionary Attack. Our main function opens the encrypted password
file and reads the contents of each line in the password file.
For each line, it splits out the username and the hashed
password. For each individual hashed password, the main functions
calls the testPass() function that tests the passwords against
a dictionary file. 

The function, testPass(), takes the encrypted password as a parameter
and returns either after finding the password or exhausting the words
in the dictionary. Notice that the function first strips the salt 
from the first two characters of the password hash. Next, it opens the 
dictionary and iterates through each word, creating an exnrypted password
hash from the dictionary word and the salt. 

If the result matches our encrypted password hash, the function prints
a message indicating the found password and returns. Others, it 
continues to test every word in the dictionary.
'''
import crypt


def testPass(cryptPass):
    salt = cryptPass[0:2]
    dictFile = open('dictionary.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, salt)
        if cryptWord == cryptPass:
            print('Found Password:' + word + '\n')
            return
    print('Password Not Found.\n')
    return


def main():
    passFile = open('passwords.txt')
    for line in passFile.readlines():
        if ':' in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print('Cracking Password For: ' + user)
            testPass(cryptPass)


if __name__ == '__main__':
    main()
