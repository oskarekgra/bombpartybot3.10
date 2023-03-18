#!/usr/bin/env python
from random import randint
import pyperclip
import sys

'''CHANGE TO YOUR OWN PATH'''
path = "C:/Users/oskar/Desktop/bombpartycheat-master/web2"

''' BOMB PARTY BOT'''

with open(path, encoding="utf8") as wordlistone:
    stringone = wordlistone.read()

while True:
    arrayOfWords = []
    print("------------------------------")
    print("type exit to close program")
    var = input("Please enter part of a word: ")

    if var == "exit":
        wordlistone.close()
        sys.exit(0)

    for line in stringone.splitlines():
        if var in line:
            arrayOfWords.append(line)

    matchingWord = arrayOfWords[randint(0,len(arrayOfWords))]
    pyperclip.copy(matchingWord)
    print(matchingWord)

wordlistone.close()
