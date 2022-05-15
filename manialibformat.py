# -*- coding: utf-8 -*-
"""
Created on Sun May  8 21:16:29 2022

@author: cinephos
"""

# This function retrieves the text from manialib formatted string 
def remove(input_string):
    
    next_char = ""
    colors = ['A','B','C','D','E','F','a','b','c','d','e','f', \
              '0','1','2','3','4','5','6','7','8','9']
    output_string = ""

#   this for loop reads every character in the string and takes action
#   when special characters appear.

    for element in input_string:
        if next_char == "":
            if element == "$":
                next_char = 'special'
                continue
            else:
                
#               A new character is added to the string. If the character 
#               is a backslash, then a second backslash is added.
#               This problem is addressed by remove backslash function.
                
                output_string = output_string + element
        if next_char == 'special':
            if element in colors:
                next_char = 'color2'
                continue
            if element == "l":
                next_char = 'link'
                continue
            else: 
                next_char = ""
                continue
        if next_char == 'color2':
            next_char = 'color3'
            continue
        if next_char == 'color3':
            next_char = ""
            continue
        if (next_char == 'link' and element == "]"):
            next_char = ""
            continue    
    return(output_string)

# This function removes extra backslash

def removebackslash(inputstring):

    
    i = inputstring.encode().decode('unicode_escape').encode("raw_unicode_escape")
    finalstring = i.decode('utf8')

    return(finalstring)
