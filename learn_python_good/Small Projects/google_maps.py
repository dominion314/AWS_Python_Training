'''Open google maps using an address in CLI'''

import webbrowser, sys
import pyperclip #Gets clipboard content
import requests 

if len(sys.argv) > 1:
    #Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    #Handle the clipborad content and lanch the browser.sys
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place' + address)

