'''
Fibonacci
'''

import sys 

print('''Fibonacci sequence begins with 0 and 1
and the next number is the sum of the previous
two numbers. The sequence continues forever...''')

while True: # Main program loop
    while True: # Keep asking until user enters valid input
        print('Enter the Nth Fibonnaci number you with to calculate')
        print('such as 5,50,1000,9999) or QUIT to quit:')
        response = input('>').upper()
        
        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        
        if response.isdecimal() and int(response) != 0:
            nth =int(response)
            break # Exit the loop when the user enters a valid number
        
        print('Please enter a number greater than 0, or QUIT')
    print()
    
    # Handle the special cases if the user enter 1 or 2
    if nth == 1:
        print('0')
        print()
        print('The #1 Fibonnaci number is 0.')
        continue
    elif nth == 2:
        print('0, 1')
        print()
        print('The #2 Fibonnaci number is 1.')
        continue
    
    # Display warning if the user entered a large number
    if nth >= 10000:
        print('WARNINGL This will take a while to display in the')
        print('screen. If you want to quit this program before it is')
        print('done, press Ctrl-C.')
        input('Press enter to begin...')
    
    # Calculate the Nth Fibonacci number
    secondToLastNumber = 0
    lastNumber = 1
    fibNumbersCalculated = 2
    print('0, 1, ', end='') # Display the first two fibonacci numbers
    
    # Display all the later numbers of the Fibonnaci sequence
    while True:
        nextNumber = secondToLastNumber + lastNumber
        fibNumbersCalculated += 1
        
        # Display the next number inthe sequence
        print(nextNumber, end='')
        
        # Check if we've found the Nth number the user wants
        if fibNumbersCalculated == nth:
            print()
            print()
            print(' The # ', fibNumbersCalculated, ' Fibonacci ',
                  'number is ', nextNumber, sep='')
            break
        
        # Print a comma in a beteen the sequence numbers
        print(', ', end='')
        
        # Shift the last two numbers
        secondToLastNumber = lastNumber
        lastNumber = nextNumber