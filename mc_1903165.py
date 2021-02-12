import sys

# ------------------------------------------------------------------------------

### Note: Allow the program to be run from the command line:


##  You can simply use the default message and key given in the program

#       python caesar_cipher.py


##  You can also use message and key given in command line in Terminal (not required),

##  where, atestmessage is the message (no space!), 4 is the key (an integer for Caesar cipher!)

#       python caesar_cipher.py atestmessage 4


# the alphabet with all symbols in the set can be encrypted
LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def caesar_cipher(message, mode, key):
    # stores the encrypted/decrypted form of the message
    ciphertext = ''

    # run the encryption/decryption code on each symbol in the message string
    for symbol in message:
        if symbol in LETTERS:
            # get the encrypted (or decrypted) index of this symbol in the LETTERS
            num = LETTERS.find(symbol)  # index of the uncoded symbol in LETTERS
            if mode == 'encrypt':
                num = num + key
            elif mode == 'decrypt':
                num = num - key
            else:
                print('Correct operation mode is needed')
                exit()

            # handle the wrap-around if num is larger than the length of LETTERS or less than 0
            num = num % len(LETTERS)

            # add encrypted/decrypted number's symbol at the end of translated
            ciphertext = ciphertext + LETTERS[num]

        else:
            # just add the symbol without encrypting/decrypting if it is not in the set LETTERS
            ciphertext = ciphertext + symbol

    # print the encrypted/decrypted string to the screen
    return ciphertext


def monoalphabetic_cipher(message, mode, key):
    # The body of this function is to be completed by you in your own python program
    ciphertext = ''
    for symbol in message:
        if symbol in LETTERS:

            if mode == 'encrypt':
                num = LETTERS.find(symbol)
                ciphertext = ciphertext + key[num]
            elif mode == 'decrypt':
                num = key.find(symbol)
                ciphertext = ciphertext + LETTERS[num]
            else:
                print('Correct operation mode is needed')
                exit()
        else:
            ciphertext = ciphertext + symbol
    return ciphertext


if __name__ == '__main__':

    # Determine the number of arguements in the command line
    numArgv = len(sys.argv)

    # the default string to be encrypted/decrypted
    message = 'a secret message.'

    # the default key used by the caesar cipher
    # key = 3
    ##  Note that for the monoalphebatic cipher you should use the following default key
    ##  by uncommenting the following statement
    key = 'jklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi'

    if numArgv == 2:
        # get the message from the input given in the command line
        message = sys.argv[1]
    elif numArgv == 3:
        # get the message and key specified the input given in the command line
        message = sys.argv[1]
        key = sys.argv[2]

    elif numArgv > 3:
        # Instruction on providing message and key from command line
        print('+++Please input the exected message and key with correct format')
        print('+++python caesar_cipher.py my_message key')
        print('+++where no space in my_message, key needs to be an integer for caesar cipher')

        print('+++For example: ')
        print('+++python caesar_cipher.py my_secrete_message 3')

        exit()

    # tells the program to encrypt or decrypt
    mode = 'encrypt'  # set to 'encrypt' or 'decrypt'
    ciphertext = monoalphabetic_cipher(message, mode, key)

    mode = 'decrypt'
    decrypttext = monoalphabetic_cipher(ciphertext, mode, key)

    ### Note: don't change the following code in your own program for displaying program outputs!!!
    print('##############################################')
    print('Cipher with key: ', key)
    print('##############################################')
    print('Plain message: ', message)
    print('Ciphertext: ', ciphertext)
    print('Decrypted text: ', decrypttext)
