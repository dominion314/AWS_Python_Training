'''
Find Pi to the Nth digit
'''

from mpmath import mp

mp.dps = input('Enter the number of digits you would like to calculate Pi to...')
if (mp.dps) > 100:
    print('Stuff')
    input()

print(mp.dps)


