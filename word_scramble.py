import random
import re
import sys


def bank(words):
    temp = words
    random.shuffle(temp)
    return temp


def scramble(words):
    scrambled = []
    for w in bank(words):
        scrambled.append(''.join(bank(list(w.lower()))))
    return scrambled


def print_words(title, words):
    print('== %s ==' % title)
    for w in words:
        print(w)
    print


def print_answer(words):
    numbered = []
    for i in range(len(words)):
        w = u'%d.\u00A0%s' % (i + 1, words[i])
        numbered.append(w.encode('utf-8'))
    print('== Answer ==')
    print('Answers:\t%s' % '  '.join(numbered))


if __name__ == '__main__':
    words = re.split('\W+', sys.argv[1].strip())
    print_words('Word Bank', bank(words))
    print_words('Scrambled', scramble(words))
    print_answer(words)
