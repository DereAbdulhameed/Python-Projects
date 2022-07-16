# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 08:16:24 2022

@author: HP
"""

''' An acronym is a short form of a word that is usually created from long words e.g.
 NLP for Natural Language Processing, AI for Artificial Intelligence etc. 
 Here is a simple python program that helps to generate acronyms
'''

user_input = str(input('Kindly enter the desired phrase: '))
words = user_input.split()
acronym = ""

for word in words:
    acronym = acronym + str(word[0]).upper()
print(acronym)



