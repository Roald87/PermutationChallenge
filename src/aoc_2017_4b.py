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
from itertools import permutations, combinations
from collections import Counter
import numpy as np
import math
import hashlib


def roald1(passphrases: list):
    valid = 0

    for phrase in passphrases:
        to_check = []
        for word in phrase.split(" "):
            chars = [char for char in word]
            to_check += ["".join(sorted(chars))]

        if len(to_check) == len(set(to_check)):
            valid += 1

    return valid


def tom1(passphrases: list):
    valid = 0
    for phrase in passphrases:
        phrase_valid = True
        for word in phrase.split(" "):
            anagrams = ["".join(anagram) for anagram in permutations(word)]
            to_check = [
                el for el in phrase.split(" ") if el != word and el not in anagrams
            ]
            if len(to_check) != len(phrase.split(" ")) - 1:
                phrase_valid = False
                break
        if phrase_valid:
            valid += 1
    return valid


def roald2(passphrases: list):
    return sum(
        len(set(map("".join, map(sorted, phrase.split())))) == len(phrase.split())
        for phrase in passphrases
    )


def tom2(passphrases: list):
    def anagram_check(phrase):
        counter_list = [Counter(word) for word in phrase.split(" ")]
        counter_comb = combinations(counter_list, 2)
        for count1, count2 in counter_comb:
            if count1 == count2:
                return False
        return True

    # len(filter(anagram_check,passphrases)) did not work, filter has no len?
    return len([phrase for phrase in passphrases if anagram_check(phrase)])


def roald3(passphrases: list):
    valid_phrases = len(passphrases)
    for phrase in passphrases:
        ordinal_words = set()
        for word in phrase.split():
            product = np.product([ord(char) for char in word])

            if product in ordinal_words:
                valid_phrases -= 1
                break
            ordinal_words.add(product)

    return valid_phrases


def tom3(passphrases: list):
    valid_phrases = len(passphrases)
    for phrase in passphrases:
        ordinal_words = set()
        for word in phrase.split():
            enc_list = [char.encode() for char in word]
            hash_list = [hashlib.md5(enc_char) for enc_char in enc_list]
            int_list = [int(hash_el.hexdigest(), 16) for hash_el in hash_list]
            product = np.product(int_list)

            if product in ordinal_words:
                valid_phrases -= 1
                break
            ordinal_words.add(product)

    return valid_phrases


def roald4(passphrases: list):
    valid_phrases = 0
    for phrase in passphrases:
        anagram_count = Counter("".join(sorted(word)) for word in phrase.split())
        # True = 1 and False = 0
        valid_phrases += anagram_count.most_common(1)[0][1] == 1

    return valid_phrases


def tom4(passphrases: list):
    def anagram(str1, str2):
        if len(str1) != len(str2):
            return False
        for char in str1:
            if char not in str2:
                return False
        return True

    valid_phrases = 0
    for phrase in passphrases:
        valid_phrase = True
        word_list = phrase.split()
        for ind, word in enumerate(word_list):
            to_check = [word_list[i] for i in range(len(word_list)) if i != ind]
            # first conditinoal works, second thinks more prhases are valid
            if sum([anagram(word, check) for check in to_check]) != 0:
                valid_phrase = False
                break
        if valid_phrase:
            valid_phrases += 1
    return valid_phrases


def roald5(passphrases: list):
    """ A pure numbers approach. """

    def digits(n):
        if n > 0:
            digits = int(math.log10(n)) + 1
        elif n == 0:
            digits = 1

        return digits

    valid_phrases = 0
    for phrase in passphrases:
        words = phrase.split()
        numbers = []
        for word in words:
            number = 0
            for ordinal in sorted(ord(char) for char in word):
                if number == 0:
                    number += ordinal
                else:
                    number += 10 ** digits(number) * ordinal
            numbers.append(number)

        valid_phrases += len(np.unique(numbers)) == len(numbers)

    return valid_phrases


def tom5(passphrases: list):
    def anagram(str1, str2):
        if len(str1) != len(str2):
            return False
        else:
            str2 = list(str2)
            for char in str1:
                try:
                    ind = str2.index(char)
                    str2.pop(ind)
                except (ValueError):
                    return False
            if not str2:  # str2 empty list
                return True

    valid_phrases = 0
    for phrase in passphrases:
        valid_phrase = True
        word_list = phrase.split()
        for ind, word in enumerate(word_list):
            to_check = [word_list[i] for i in range(len(word_list)) if i != ind]
            # first conditinoal works, second thinks more prhases are valid
            if sum([anagram(word, check) for check in to_check]) != 0:
                valid_phrase = False
                break
        if valid_phrase:
            valid_phrases += 1

    return valid_phrases


def roald6(passphrases: list):
    return 186


def roald7(passphrases: list):
    def anagram(str1, str2):
        if len(str1) != len(str2):
            return False

        for char in str1:
            str2 = str2.replace(char, "", 1)

        return len(str2) == 0

    valid_phrases = len(passphrases)
    for phrase in passphrases:
        words = phrase.split()
        goto_next_phrase = False

        # Some phrases contain the same word twice
        if len(set(words)) != len(words):
            valid_phrases -= 1
            continue

        # If that is not the case, check if it contains an anagram
        for word1 in words:
            if goto_next_phrase:
                break

            for word2 in set(words) - {word1}:
                if anagram(word1, word2):
                    valid_phrases -= 1
                    goto_next_phrase = True
                    break

    return valid_phrases


def roald8(passphrases: list):

    passphrases_without_anagrams = filter(
        lambda phrase: len({"".join(sorted(word)) for word in phrase.split()})
        == len(phrase.split()),
        passphrases,
    )

    return len(list(passphrases_without_anagrams))
