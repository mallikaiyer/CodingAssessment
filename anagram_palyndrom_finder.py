#!/usr/bin/env python

import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from Strings_Anagrams_Palindromes import WordLengthError, NotPalindromeError, EmptyStringError, MyStringClass, Anagram, Palindromes

def get_words_from_page(url):
	'''
	Extracts all words from a webpage and returns them as a list.
	Input: webpage url
	Output: list of words
	'''
	page = urlopen(url)
	html = page.read().decode("utf-8")
	soup = BeautifulSoup(html, "html.parser")
	text = soup.get_text()
	list_of_words = re.findall('[a-zA-Z]+', text)

	return list_of_words

def get_anagrams_in_list(list_of_words):
	'''
	For each word in the input list, the function will identify all its anagrams from the list.
	Input: list of words
	Output: list of lists, where each element of the outer list is itself a list of words from the input that are anagrams of each other
	Note: Words that are the same except for capitalization will be considered anagrams of each other. 
	Words that do not have anagrams are not included in the output.
	'''
	anagrams_in_list = []
	list_of_words_uniq = set(list_of_words)
	for w in list_of_words_uniq:
		anagrams_of_word_in_list = tuple(sorted([s for s in list_of_words_uniq if sorted(list(s.lower())) == sorted(list(w.lower()))])) # Compares the list of characters in the two words.
		# Characters must be sorted to be in the same order, or the lists will not be considered equal.
		anagrams_in_list.append(anagrams_of_word_in_list)
	anagrams_in_list_2 = [list(i) for i in set(anagrams_in_list) if len(i) >1]

	return anagrams_in_list_2

def get_palindromes_in_list(list_of_words):
	'''
	Identifies all palindromes from a list of words.
	Input: list of words
	Output: list of palindromes
	'''
	palindromes_in_list= set([])
	for w in list_of_words:
		word = MyStringClass(w)
		mirroredWord = word.mirror()
		if mirroredWord.lower() == w.lower() and len(w) > 1:
			palindromes_in_list.add(w)

	return list(palindromes_in_list)


if __name__ == '__main__':

	'''
	Identifies anagrams and palindromes from the webpage given as input.
	# Input: url of webpage from which anagrams and palindromes must be found.
	# Output: (1) List of palindromes. (2) List of Anagrams (see get_anagrams_in_list for detailed desc. of output.) 
	'''
	
	webUrl = sys.argv[1]
	wordsList = get_words_from_page(webUrl)
	pagePalindromes = get_palindromes_in_list(wordsList)
	print("Palindromes in the webpage: {}".format(pagePalindromes))
	print("")
	pageAnagrams = get_anagrams_in_list(wordsList)
	print("Anagrams in the webpage: {}".format(pageAnagrams))
