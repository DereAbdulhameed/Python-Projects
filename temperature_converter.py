# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 07:15:40 2022

@author: HP
"""
''' This is a project for the MacroTutor assessment. A temperature converter which takes in
the temperature in Fahrenheit and converts it into celsius.

The Formula for converting Fahrenheit into celsius is (F - 32) * 5/9'''


Fahrenheit = int(input('Enter your desired temperature in Fahrenheit that you will like to convert: '))
celsius = (Fahrenheit - 32) * 5/9 

print('The converted temperature in celsius is', format(celsius))