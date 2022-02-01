'''
Digital Clock
Displays a digital clock with current time.
'''

import sys, time
import seven_seg # Import seven_seg script

try:
    while True: # Main program loop
        # CLear the screen by printing several new lines
        print('\n' * 60)

except KeyboardInterrupt:
    print('Digital Clock')
    sys.exit() # When Ctrl-C is pressed, end the program 