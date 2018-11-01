import re
import sys

# Compatible with both python 2 and 3
inp = input if sys.hexversion >= 0x3000000 else raw_input

VOWELS = set('aeiouyAEIOUY')
YS = set('yY')

def pig_word(word):
    """
    Given a word, convert it to Pig Latin
    """
    if hasattr(word, 'group'):
        # pull the text out of a regex match object
        word = word.group()

    # find the first vowel and what it is
    vowel, where = None, None
    for i,ch in enumerate(word):
        if ch in VOWELS:
            vowel, where = ch, i
            break

    if vowel is None:
        # No vowels found
        return word
    elif where == 0 and vowel not in YS:
        # Starts with a vowel - end in 'way'
        #   (leading y is treated as a consonant)
        return word + 'way'
    else:
        # Starts with consonants - move to end and follow with 'ay'

        # check capitalization
        uppercase = word.isupper() and len(word) > 1
        titlecase = word[:1].isupper() and not uppercase

        # rearrange word
        word = word[where:] + word[:where] + 'ay'

        # repair capitalization
        if uppercase:
            word = word.upper()
        elif titlecase:
            #str.title() does not work words with apostrophes
            word = word[:1].upper() + word[1:].lower()

        return word

def pig_latin(s, reg=re.compile('[a-z\']+', re.IGNORECASE)):
    """
    Translate a word into Pig Latin
    """
    # find each word , pass it to pig_word, and insert the result back into the string
    return reg.sub(pig_word, s)

def main():
    while True:
        s = inp('Enter a word to translate (or Enter to quit): ')
        if s.strip():
            print(pig_latin(s))
            print('')
        else:
            break

if __name__=="__main__":
    main()
