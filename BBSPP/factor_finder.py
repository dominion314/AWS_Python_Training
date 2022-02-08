'''
Factor Finder - Finds all the factors of a number
'''

import math, sys

print('''Factor Finder
A numbers factors are two number that, when multiplied with each
other, produce the number. If a number only has two factors, we call that
a prime number. Otherwise its called a composite number''')

while True: # Main program loop
    print('Enter a positive whole number to factor (or QUIT):')
    response = input('> ')
    if response.upper() ==  'QUIT':
        sys.exit()
        
    if not (response.isdecimal() and int(response) > 0):
        continue
    number = int(response)
    
    factors = []
    
    # Find the factors of number
    for i in range(1, int(math.sqrt(number)) +1):
        if number % i == 0: # If theres no remainder, it is a factor
            factors.append(i)
            factors.append(number // i)
            
    # Convert to a set to get rid of diplicate factors
    factors = list(set(factors))
    factors.sort()
    
    # Display the results
    for i, factor in enumerate(factors):
        factors[i] = str(factor)
    print(', '.join(factors))
    
