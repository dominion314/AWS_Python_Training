'''
Sevseg
A seven-segment number display module, used for calculator and digital clock programs.
'''

"""A labeled seven-segment display, with each segment labeled A to G:
  __A__
 |     |    Each digit in a seven-segment display:
 F     B     __       __   __        __   __  __   __   __
 |__G__|    |  |   |  __|  __| |__| |__  |__    | |__| |__|
 |     |    |__|   | |__   __|    |  __| |__|   | |__|  __|
 E     C
 |__D__|"""

def getSevSegStr(number, minWidth=0):
    '''Return a seven-segment display string of the number
    The returned string will be padded with zeroes if 
    it is smaller thatn the minWidth'''

    # Conver number to string in case its an int or float

    number = str(number).zfill(minWidth)

    rows = ['', '', '']
    for i, numeral in enumerate(number):
        if numeral == '.': # Render the decimal point
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += '.'
            continue # Skip space in between digits
        elif numeral == '-': # Render the negative sign
            rows[0] += '    '
            rows[1] += ' __ '
            rows[2] += '    '
        elif numeral == '0':  # Render the 0.
            rows[0] += ' __ '
            rows[1] += '|  |'
            rows[2] += '|__|'
        elif numeral == '1':  # Render the 1.
            rows[0] += '    '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '2':  # Render the 2.
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += '|__ '
        elif numeral == '3':  # Render the 3.
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += ' __|'
        elif numeral == '4':  # Render the 4.
            rows[0] += '    '
            rows[1] += '|__|'
            rows[2] += '   |'
        elif numeral == '5':  # Render the 5.
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += ' __|'
        elif numeral == '6':  # Render the 6.
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += '|__|'
        elif numeral == '7':  # Render the 7.
            rows[0] += ' __ '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '8':  # Render the 8.
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += '|__|'
        elif numeral == '9':  # Render the 9.
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += ' __|'
        
        # Add a space (for the space in between numerals) if this 
        # isn't the last numeral

        if i != len(number):
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += ' '
    
    return '\n'.join(rows)

# If this program isn't being imported, display the number 00 to 99

if __name__ == '__main__':
     print('This module is meant to be imported rather than run.')
     print('For example, this code:')
     print('    import sevseg')
     print('    myNumber = sevseg.getSevSegStr(42, 3)')
     print('    print(myNumber)')
     print()
     print('...will print 42, zero-padded to three digits:')
     print(' __        __ ')
     print('|  | |__|  __|')
     print('|__|    | |__ ')