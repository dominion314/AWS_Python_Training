'''

Web scraping is the term for using a program to download and process content from the web.
Gets a street address from the command line arguments or clipboard
Opens the web browser to the Google Maps page for the address

This means your code will need to do the following:

-Read the command line arguments from sys.argv.
-Read the clipboard contents.
-Call the webbrowser.open() function to open the web browser.
'''

import webbrowser

webbrowser.open('https://inventwithpython.com/')



