"""
Solving Advent of Code puzzle 2017 day 4 part b:

For added security, yet another system policy has been put in place. Now, a valid
passphrase must contain no two words that are anagrams of each other - that is, a
passphrase is invalid if any word's letters can be rearranged to form any other word in
the passphrase.

For example:
 - abcde fghij is a valid passphrase.
 - abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the
 first word.
 -a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming
 another word.
 - iiii oiii ooii oooi oooo is valid.
 - oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.

Under this new system policy, how many passphrases are valid?
"""
from itertools import permutations

def roald1(passphrases: list):
    valid = 0

    for phrase in passphrases:
        to_check = []
        for word in phrase.split(' '):
            chars = [char for char in word]
            to_check += [''.join(sorted(chars))]

        if len(to_check) == len(set(to_check)):
            valid += 1

    return valid

def tom1(passphrases: list):
    valid = 0
    for phrase in passphrases:
        phrase_valid = True
        for word in phrase.split(' '):
            anagrams = [''.join(anagram) for anagram in permutations(word)]
            to_check = [el for el in phrase.split(' ') if el != word and el not in anagrams]
            if len(to_check) != len(phrase.split(' '))-1:
                phrase_valid = False
                break
        if phrase_valid:
            valid +=1
    return valid

def roald2(passphrases: list):
    return sum(
        len(set(map("".join, map(sorted, phrase.split())))) == len(phrase.split())
        for phrase in passphrases
    )
