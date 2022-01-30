
'''# Task 1 - Print splice
# Complete the function to print the first X number of characters in the given string
def printFirst(mystring, x):
# answer here
 
# expected output: WGU
printFirst('WGU College of IT', 3) 

# expected output: WGU Co
printFirst('WGU College of IT', 6)
 
# expected output: WGU College
printFirst('WGU College of IT', 11)
'''


'''
# Task 2 - String splice
# Complete the function to return the last X number of characters in the given string

# # Complete the function to return the last X number of characters
# # in the given string
def getLast(mystring, x):
#answer here

# # expected output: IT
print(getLast('WGU College of IT', 2))
 
# # expected output: College of IT
print(getLast('WGU College of IT', 13))
'''

'''
# Task 3 - Use True or False to complete the function to return True if the word WGU exists in the given string otherwise return False

# # Complete the function to return True if the word WGU exists in the given string
# # otherwise return False
def containsWGU(mystring):
#answer here
    
# # expected output: True
print(containsWGU('WGU College of IT'))
    
# # expected output: False
print(containsWGU('Night Owls Rock'))
'''

'''
# Task 4 - Use print to complete the function to print all of the words in the given string

# # Complete the function to print all of the words in the given string
def printWords(mystring):
#answer here
# # expected output: ['WGU', 'College', 'of', 'IT']
printWords('WGU College of IT')    
    
# # expected output: ['Night', 'Owls', 'Rock']
printWords('Night Owls Rock')
'''


'''
# Task 5 - Use Join method complete the function to 
# combine the words into a sentence and return a string

# Complete the function to combine the words into a sentence and return a string 
def combineWords(words):
   #answer here

# Expected output: WGU College of IT
print(combineWords(['WGU', 'College', 'of', 'IT']))
    
# Expected output: Night Owls Rock
print(combineWords(['Night', 'Owls', 'Rock']))
'''


'''
# Task 6 - Use Replace Method to complete the function to 
# replace the word WGU with Western Governors University 
# and print the new string

# Complete the function to replace the word WGU 
# with Western Governors University
# and print the new string

def replaceWGU(mystring):
    #answer here

# Expected output: Western Governors University Rocks
replaceWGU('WGU Rocks')
    
# Expected output: Hello, Western Governors University
replaceWGU('Hello, WGU')
'''


'''
# Task 7 - Use split method to complete the function 
# to remove the word WGU from the given string ONLY if 
# it's not the first word and return the new string

def removeWGU(mystring):
    if 'WGU' !=

# Expected output: WGU Rocks
print(removeWGU('WGU Rocks'))
# Expected output: Hello, John
print(removeWGU('Hello, WGUJohn'))
'''

'''
# Task 8
# Use strip method to complete the function to 
# remove trailing spaces from the first string and 
# leading spaces from the second string and return 
# the combined strings

def removeSpaces(string1, string2):
# # Student code goes here
    
# # expected output: WGU Rocks-You know it!
print(removeSpaces('WGU Rocks    ', '  -You know it!'))
    
# # expected output: Welcome WGU-IT Students
print(removeSpaces('Welcome WGU ', ' -IT Students'))
'''

'''
# Task 9
# Use the round method to coomplete the function to print the specified hourly rate with two decimals

# # Complete the function to print the specified hourly rate with two decimals
def displayHourlyRate(rate):
# # Student code goes here
    
    
# # expected output: $34.79
# displayHourlyRate(34.789123)    
 
# # expected output: $24.12
# displayHourlyRate(24.123456)
'''

'''
# Task 10
# Complete the function to return the 
# number of uppercase letters in the given string

# Complete the function to return the number 
# of uppercase letters in the given string
def countUpper(mystring):    
    count=0    
    for i in mystring:#for loop to loop all letter        
        if i.isupper():#use isupper to check if uppercase            
            count=count+1    
    return count
    '''