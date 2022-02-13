#!/usr/bin/env python
from itertools import permutations
import re

class WordLengthError(Exception):
    pass


class NotPalindromeError(Exception):
    pass
    

class EmptyStringError(Exception):
    pass
    

class MyStringClass():
    
    def __init__(self, value):
        if not type(value) == str:
            raise TypeError("Argument passed to class is not a string!")
        else:
            self.value = value

    def append(self, a):
        '''
        Method to append an input string to the MyStringClass instance.
        Returns a string object as output.
        '''
        if not type(a) == str: # First check that 'a' is of type string.
            raise TypeError("Argument passed to append is not a string!")
        else:
            return self.value+a
    
    def mirror(self):
        '''
        Method to return the mirror of the MyStringClass instance.
        Returns a string object as output.
        '''
        l = list(self.value)
        m = l[::-1]
        return ''.join(m)
    
    def remove_substring(self, subst):
        '''
        Method to remove a substring from the MyStringClass instance.
        Returns a string object as output.
        '''
        if not type(subst) == str: # First check that 'subst' is of type string.
            raise TypeError("Argument passed to remove_string is not a string!")
        elif not subst in self.value: # Then check if 'subst' is in self.value. 
            print("Warning: {} is not in {}! Returning {} as is.".format(subst, self.value, self.value))
            return self.value
        else: # If the substring is in self.value, then remove and return.
            return self.value.replace(subst, '')
    
    def read_from_file(file_name):
        '''Method to read text from a file and return it as a MyStringClass object.'''
        with open(file_name, 'r') as f:
            s = ''.join(f.readlines())
            sc = MyStringClass(s)
        return sc

    def write_to_file(self, file_name):
        '''Method to write the value of a MyStringClass instance to a file.'''
        with open(file_name, 'w') as f:
            f.write(self.value)


class Anagram(MyStringClass):
    '''Child class to process anagrams'''
    def get_anagrams(self):
        '''Returns all anagrams of a given word in the form of a list'''
        s = self.value
        return [''.join(list(i)) for i in list(permutations(s))] # list of anagrams
    

class Palindromes(MyStringClass):
    '''Class to store and process palindromes. Note: does not accept words that are not palindromes.'''
    def __init__(self, value):
        if not type(value) == str: 
            raise TypeError("Argument passed to Palindromes is not a string!")
        elif re.fullmatch(r'\s+', value): # Check if the input consists only of empty spaces.
            raise EmptyStringError("Argument passed to Palindromes cannot contain spaces only!")
        elif not len(value) > 1: # Check if the input consists of one char only.
            raise WordLengthError("Argument passed to Palindromes must have length greater than one!")
        else: # Check if the input is a palindrome.
            mirroredWord = ''.join(list(value)[::-1])
            if not mirroredWord.upper() == value.upper():
                raise NotPalindromeError("Argument passed to Palindromes is not a palindrome!")
            else:
                self.value = value